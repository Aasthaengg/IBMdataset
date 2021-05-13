n = int(input())
ab = [list(map(int, input().split())) for _i in range(n)][::-1]

r = 0
for i in range(n):
    a, b = ab[i]
    if (r+a)%b==0:
        continue
    r += b-(r+a)%b
print(r)
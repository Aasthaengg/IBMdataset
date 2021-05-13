n = int(input())
ans = 0
b = []

for i in range(n):
    b = list(map(int, input().split()))
    ans = ans + (b[1] - b[0] +1)

print(ans)

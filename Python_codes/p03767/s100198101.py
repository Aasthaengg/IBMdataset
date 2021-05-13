n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
r = 0
for i in range(n):
    r += a[2*i+1]
print(r)
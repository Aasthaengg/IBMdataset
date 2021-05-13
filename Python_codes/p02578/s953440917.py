n = int(input())
a = list(map(int, input().split()))

b = [0] * n

for i in range(n-1):
    if a[i] + b[i] > a[i+1]:
        b[i+1] += (a[i] + b[i]) - a[i+1]
ans = sum(b)
print(ans)

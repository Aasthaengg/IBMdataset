n = int(input())
a = list(map(int, input().split()))

ans = 0
amin = 10**10
for i in range(n):
    if abs(a[i] -sum(a)/n) < amin:
        amin = abs(a[i] -sum(a)/n)
        ans = i
print(ans)
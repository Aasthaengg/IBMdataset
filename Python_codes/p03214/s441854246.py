N = int(input())
a = list(map(int, input().split()))
x = sum(a)/N
y = 10**9
for i in range(N):
    if abs(x-a[i]) < y:
        y = abs(x-a[i])
        ans = i
print(ans)
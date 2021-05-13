N = int(input())
a = list(map(int, input().split()))
ave = sum(a)/N
tmp = float('inf')
ans = 0
for i in range(N-1, -1, -1):
    if abs(a[i] - ave) <= tmp:
        tmp = abs(a[i] - ave)
        ans = i
print(ans)

n = int(input())
a = [int(i) for i in input().split()]
ave = sum(a)/n
s = float("inf")
for i in range(n-1,-1,-1):
    if s >= abs(ave-a[i]):
        ans = i
        s = abs(ave-a[i])
print(ans)
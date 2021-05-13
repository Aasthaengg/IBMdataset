n, k = (int(i) for i in input().split())
cnt = 0
for x in range(k+1, n+1):
    cnt = cnt + int(n / x) * (x - k) + max(int(n % x) - (k - 1), 0)
    #print(int(n / x) * (x - k), end=" ")
    #print(max(int(n % x) - (k - 1), 0))
if k == 0:
    cnt = cnt - n
print(cnt)
n, k = map(int, input().split())
a = list(map(int, input().split()))
digits = [0]*40
for i in a:
    for j in range(40):
        digits[j] += i>>j&1
ans = 0
flg = True
for i in range(39, -1, -1):
    if flg and k>>i&1==0:
        ans += digits[i]*2**i
        continue
    ans += max(digits[i], n-digits[i])*2**i
    if flg and digits[i]>=(n+1)//2:
        flg = False
print(ans)
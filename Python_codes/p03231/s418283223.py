import fractions
n,m = map(int,input().split())
s = input()
t = input()

lcm = n*m // fractions.gcd(n,m)
ans = -1
ss = lcm // m
ts = lcm // n
j = 0
flg = True
for i in range(0,n,ss):
    if s[i] == t[j] :
        j += ts
        continue
    else:
        flg = False
        break

if flg :
    ans = lcm
print(ans)

N=int(input())
s=input()
mod = 10**9+7
d=""
cnt=N
while cnt:
    if  cnt > 1 and s[N-cnt] ==s[N-cnt+1]:
        d += "W"
        cnt -=2
    else:
        d += "H"
        cnt -=1
if d[0] == "W":
    ans = 6
else:
    ans = 3
for i in range(1,len(d)):
    if d[i-1] =="H":
        ans *= 2
    elif d[i] =="W":
        ans *= 3
    ans %= mod
print(ans)
s=input()
ans=1
ans2=1
MOD=10**9+7
for i in range(len(s)):
  if s[len(s)-1-i]=='1':
    ans=(ans*2+ans2)%MOD
  ans2=(ans2*3)%MOD
print(ans)
n,k = map(int,input().split())
s = input()
ans=[]
t = s[k-1].lower()
for i in range(0,k-1):
  ans += s[i]
ans+= t
for i in range(k,n):
  ans+=s[i]
print(''.join(ans))
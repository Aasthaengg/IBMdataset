n=int(input())
s=input()
x=[0]
for i in range(n):
  if s[i]=='I':
    a=1
  else:
    a=-1
  x.append(x[i]+a)
ans=max(x)
print(ans)
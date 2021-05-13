n=int(input())
a=str(input())
b=str(input())
c=str(input())
ans=0
for i in range(n):
  if a[i]==b[i] and b[i]==c[i]:
    ans=ans
  elif a[i]!=b[i] and b[i]!=c[i] and c[i]!=a[i]:
    ans=ans+2
  else:
    ans=ans+1
print(ans)
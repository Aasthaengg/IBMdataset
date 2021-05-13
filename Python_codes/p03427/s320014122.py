n=int(input())
s=str(n)
a=len(s)
b=(int(s[0])+1)*10**(a-1)-1
ans=9*(a-1)+int(s[0])
if n==b:
  print(ans)
else:
  print(ans-1)
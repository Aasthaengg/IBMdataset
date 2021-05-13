n=int(input())
s=input()
t=input()
if n==1 and s!=t:
  print(2)
  exit()
if n==1 and s==t:
  print(1)
  exit()
ans=2*n
for i in range(n):
  if s[i:n]==t[0:n-i]:
    ans-=n-i
    break
print(ans)
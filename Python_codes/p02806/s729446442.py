n=int(input())
s=[""]*n
t=[""]*n
for i in range(n):
  s[i],t[i]=input().split()
x=input()
for i in range(n):
  if s[i]==x:
    ans=0
    for j in range(i+1,n):
      ans+=int(t[j])
    break
print(ans)
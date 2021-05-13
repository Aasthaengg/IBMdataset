n,k=map(int,input().split())
s=input()
c=0
for i in range(1,n):
  if s[i]==s[i-1]:
    c+=1
c+=2*k
print(min(n-1,c))

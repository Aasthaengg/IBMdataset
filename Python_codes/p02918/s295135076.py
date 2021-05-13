n,k=map(int,input().split())
s=input()
c=1
for i in range(n-1):
 if s[i]!=s[i+1]:c+=1
print(n-c+min(c-1,k*2))

n,k=map(int,input().split())
s=input()
un=0
for i in range(1,len(s)):
  if s[i-1]!=s[i]:
    un+=1
print((n-1)-max(0,un-2*k))
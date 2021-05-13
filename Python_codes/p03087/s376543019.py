n,q=map(int,input().split())
s=input()
num=[0]
be=""

for i in range(n):
  if be=="A" and s[i]=="C":
    num.append(num[-1]+1)
    
  else:
    num.append(num[-1])
    
  be=s[i]
    
for i in range(q):
  l,r=map(int,input().split())
  
  print(abs(num[l]-num[r]))
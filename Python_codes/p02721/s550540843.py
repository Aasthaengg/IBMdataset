def sep():
    return map(int,input().strip().split(" "))
def lis():
    return list(sep())
import sys
sys.setrecursionlimit(10**6)

n,k,c=sep()
s=input()
c1=[0]*(n+5)
c2=[0]*(n+5)
for i in range(n):
    if s[i]=="x":
        c1[i]=c1[i-1]
    else:
        c1[i]=max(c1[i-1],c1[i-c-1]+1)
for i in range(n-1,-1,-1):
    if s[i]=="x":
        c2[i]=c2[i+1]
    else:
        c2[i]=max(c2[i+1],c2[(i+c+1)%n]+1)
ans=[]
if c2[1]==k-1 and s[0]=="o":
    ans.append(1)

for i in range(1,n-1):
    if s[i]=="x":
        continue
    if c1[i-1] + c2[i+1]==k-1:
        ans.append(i+1)

if n!=1:
    if c1[n-2]==k-1 and s[0]=="o":
        ans.append(n)

for i in ans:
    print(i)



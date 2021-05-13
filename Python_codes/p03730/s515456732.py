A,B,C=map(int,input().split())
x=[]
ans="NO"
for i in range(B):
    x.append((A*i) % B)
    
if C in x:
    ans="YES"
print(ans)
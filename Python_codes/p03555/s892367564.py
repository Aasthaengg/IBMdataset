C=[0,0]
C[0]=list(map(str,input()))
C[1]=list(map(str,input()))
ans="NO"
X=C[0][::-1]
if C[1]==X:
    ans="YES"
print(ans)
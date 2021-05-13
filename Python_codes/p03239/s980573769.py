n,t=map(int,input().split())
c=1001
for i in range(n):
    cn,tn=map(int,input().split())
    if tn<=t:
        if cn<c:
             c=cn
if c==1001:
    print("TLE")
else:
    print(c)
S=int(input())
MOD=10**9
if S%MOD==0:
    s=0
else:
    s=MOD-S%MOD

X1,Y2=s,1
Y1=10**9
X2=(S+X1)//Y1

print(0,0,X1,Y1,X2,Y2)

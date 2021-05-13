L=input()
lenl=len(L)
mod=10**9+7

a=0
b=1
newa=0
newb=0

for i in range(lenl):
    if L[i]=="0":
        a,b=a*3%mod,b%mod
    else:
        a,b=(3*a+b)%mod,2*b%mod
    #print(a,b)
print((a+b)%mod)


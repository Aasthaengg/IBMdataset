# KPC2020-A
def ceilT(a,b): #ceil(a/b)
    return (a+b-1)//b
H=int(input())
W=int(input())
N=int(input())
e=max(H,W)
print(ceilT(N,e))
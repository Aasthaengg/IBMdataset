T1, T2 = map(int,input().split())
A1, A2 = map(int,input().split())
B1, B2 = map(int,input().split())

A1 *= T1
B1 *= T1
A2 *= T2
B2 *= T2

if A1+A2 > B1+B2: # Aを遅く
    A1,B1 ,A2,B2 = B1,A1 ,B2,A2

if A1+A2 == B1+B2:
    print("infinity")
    exit()

if A1 < B1:
    print(0)
    exit()

def nibu(l,r):
    if l >= r:
        return l
    c = (l+r+1)//2
    if (A1+A2)*(c-1)+A1 >= (B1+B2)*(c-1)+B1:
        return nibu(c,r)
    else:
        return(nibu(l,c-1))

ans = nibu(0,10**100)
if (A1+A2)*(ans-1)+A1 == (B1+B2)*(ans-1)+B1:
    print(ans*2-2)
else:
    print(ans*2-1)
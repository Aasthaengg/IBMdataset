from math import gcd

def lcm(a,b):
    return (a*b)//gcd(a,b)
N,M=map(int, input().split())
S=input()
T=input()

L=lcm(N,M)

i=0
j=0
while 0<=i<N and 0<=j<M:
    nowi=i*(L//N)
    nowj=j*(L//M)
    #print(i,j,nowi,nowj)
    if nowj==nowi:
        if S[i]!=T[j]:

            print(-1)
            exit()

    if nowi>nowj:
        j+=1
    elif nowi<nowj:
        i+=1
    else:
        i+=1
        j+=1
print(L)
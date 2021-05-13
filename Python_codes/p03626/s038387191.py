N=int(input())
S1=input()
S2=input()
pr=10**9+7
t=0
a=1
c=0
while t<N:
    if S1[t]==S2[t]:
        a=a*(3-c)%pr
        t+=1
        c=1
    else:
        if c==0:
            a=6
        elif c==1:
            a=a*2%pr
        else:
            a=a*3%pr
        t+=2
        c=2
print(a)
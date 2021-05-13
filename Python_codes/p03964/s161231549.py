N = int(input())
t,a = map(int,input().split())
for _ in range(N-1):
    T,A = map(int,input().split())
    b = 1
    if t>T:
        if t%T==0:
            b = t//T
        else:
            b = t//T+1
    T0 = T*b
    A0 = A*b
    c = 1
    if a>A0:
        if a%A0==0:
            c = a//A0
        else:
            c = a//A0+1
    T0 = T0*c
    A0 = A0*c
    c = 1
    if a>A:
        if a%A==0:
            c = a//A
        else:
            c = a//A+1
    T1 = T*c
    A1 = A*c
    b = 1
    if t>T1:
        if t%T1==0:
            b = t//T1
        else:
            b = t//T1+1
    T1 *= b
    A1 *= b
    if T0<=T1:
        t,a = T0,A0
    else:
        t,a = T1,A1
print(t+a)
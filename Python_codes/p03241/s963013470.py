N,M = map(int,input().split())
amax = 1
for i in range(1,int(M**0.5)+1):
    if M%i==0:
        b = i
        c = M//i
        if b>=N and c>=N:
            a = max(b,c)
        elif c<N<=b:
            a = c
        elif b<N<=c:
            a = b
        else:
            a = 1
        amax = max(amax,a)
print(amax)
N,M = map(int,input().split())
amax = 1
for i in range(1,int(M**0.5)+1):
    if M%i==0:
        a = i
        b = M//i
        if b>=N:
            amax = max(amax,a)
        a,b = b,a
        if b>=N:
            amax = max(amax,a)
print(amax)
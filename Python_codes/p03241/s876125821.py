N,M = map(int,input().split())
g = 0
for i in range(1,int(M**0.5)+1):
    if M%i==0:
        a = i
        b = M//i
        if a>=N:
            g = max(g,b)
        if b>=N:
            g = max(g,a)
print(g)
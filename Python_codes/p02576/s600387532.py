N,X,T = map(int,input().split())
s = 0;t = 0
while s<N:
    t += T
    s += X
print(t)
R,G,B,N=map(int,input().split())
c=0
for r in range(3000+1):
    for g in range(3000+1):
        n=N-r*R-G*g
        if n>=0:
            c+=n%B==0
print(c)

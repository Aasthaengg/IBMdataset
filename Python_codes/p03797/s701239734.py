n,m=map(int,input().split())
if 2*n>=m:
    print(m//2)
else:
    k1 = (m-n*2)//4
    k2 = k1+1
    k3 = max(k1-1,0)
    r1 = min(n+k1,(m-k1*2)//2)
    r2 = min(n+k2,(m-k2*2)//2)
    r3 = min(n+k3,(m-k3*2)//2)
    print(max(r1,r2,r3))

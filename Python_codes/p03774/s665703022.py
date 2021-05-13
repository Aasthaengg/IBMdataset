n,m = map(int,input().split())
A = {}
for i in range (1,n+1):
    a,b = map(int,input().split())
    A[i] = [a,b]

B = {}
for i in range(1,m+1):
    c,d = map(int,input().split())
    B[i] = [c,d]

for v in A.values():
    t = float('inf')
    ans = 0
    for x,w in B.items():
        if abs(v[0]-w[0])+abs(v[1]-w[1]) < t:
            t = abs(v[0]-w[0])+abs(v[1]-w[1])
            ans = x
    print (ans)

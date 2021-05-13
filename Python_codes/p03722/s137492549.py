n , m = map(int,input().split())
ainf = -334334334334334334334334
es = []

def bf():
    d = [ainf] * n
    d[0] = 0
    i = 0 
    sa = 0
    ta = 0
    
    for i in range(n+1):
        for p,q,r in es:
            if d[p] != ainf and d[q] < d[p] + r:
                d[q] = d[p] + r
                if i == n-1:
                    sa = d[n-1]
                if i == n:
                    ta = d[n-1]
                
    return sa,ta,d[n-1]

for _ in range(m):
    x , y , z = map(int,input().split())
    es.append([x-1,y-1,z])
    
s,t,u = bf()

if s == t:
    print(u)
else:
    print("inf")
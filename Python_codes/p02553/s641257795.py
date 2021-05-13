a,b,c,d = map(int,input().split())
A = set()
B = set()
A.add(a)
A.add(b)
B.add(c)
B.add(d)
for i in {-1,0,1}:
    A.add(i)
    B.add(i)

o = set()
for j in A:
    for k in B:
        if a <= j <= b and c <= k <= d:
            o.add(j*k)
print(max(o))
N,Q = map(int, input().split())
S = input().strip()
a = []
p = ""
c = 0
for i,v in enumerate(S):
    if p == 'A' and v == 'C':
        c += 1
    a.append(c)
    p = v

for i in range(Q):
    l,r = map(int,input().split())
    print(a[r-1] - a[l-1])


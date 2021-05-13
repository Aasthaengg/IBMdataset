n,k = map(int,input().split())
di = [0]*(10**5)
for i in range(n):
    a,b = map(int,input().split())
    di[a-1] += b
q = 0
p = 0
while True:
    q += di[p]
    if k <= q:
        print(p +1)
        break
    p += 1
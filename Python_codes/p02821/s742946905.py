from bisect import bisect_left

N,M= [int(i) for i in input().split()]
n = sorted([int(x) for x in input().split()])

s =[0]*(N+1)
s[0]=n[0]
for i in range(1,N+1):
        s[i] = s[i-1]+n[i-1]
MM=n[-1]*2
mm=n[0]*2

while True:
        c=0        
        r=(mm+MM)//2
        for i in range(N):
                c += N-bisect_left(n,r-n[i])
        if (MM-mm) < 2:
                break
        elif c>=M:
                mm=r
        elif c<M:
                MM=r

v=0
for i in range(N):
        j=bisect_left(n,r-n[i])
        v+= (s[N] - s[j]) + (N-j)*n[i]

v = v - (c-M)*(r)

print(v)        
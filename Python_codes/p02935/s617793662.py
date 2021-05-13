N=int(input())
v=list(map(int,input().split()))
v.sort()
pot=v[0]
for i in range(1,N):
    pot = 0.5*(pot + v[i])

print(pot)
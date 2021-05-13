N=int(input())
P=[0]+list(map(int,input().split()))

X=0
for i in range(1,N+1):
    X+=(i!=P[i])

if X<=2:
    print("YES")
else:
    print("NO")
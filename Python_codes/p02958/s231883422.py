N=int(input())
p=list(map(int,input().split()))

li=[i for i in range(1,N+1)]

for j in range(N):
    for k in range(N):
        p[j],p[k]=p[k],p[j]
        if p==li:
            print("YES")
            exit()
        else:
            p[j],p[k]=p[k],p[j]

print("NO")

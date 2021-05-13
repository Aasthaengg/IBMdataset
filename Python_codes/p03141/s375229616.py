N=int(input())
AB=[list(map(int,input().split())) for i in range(N)]
b=-sum(AB[i][1] for i in range(N))
AB.sort(key=lambda x:x[0]+x[1],reverse=True)
for i in range(N):
    if i%2==0:
        b+=sum(AB[i])
print(b)
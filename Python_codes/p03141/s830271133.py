n=int(input())
c=[list(map(int, input().split())) for i in range(n)]

for i in range(n):
    c[i].append(c[i][0]+c[i][1])

c.sort(key=lambda x:x[2],reverse=True)

ans1=0
ans2=0

for i in range(n):
    if i%2==0:
        ans1+=c[i][0]
    else:
        ans2+=c[i][1]

print(ans1-ans2)
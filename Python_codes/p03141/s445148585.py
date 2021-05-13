n=int(input())
ab=[list(map(int, input().split())) for _ in range(n)]
yusendo=[]
for i in range(n):
    yusendo.append([ab[i][0]+ab[i][1], ab[i][1]-ab[i][0], i])
yusendo.sort(reverse=True)
# print(yusendo)

takahashi=0
aoki=0
for i in range(n):
    if i%2==0:
        takahashi+=ab[yusendo[i][2]][0]
    else:
        aoki+=ab[yusendo[i][2]][1]
# print(takahashi, aoki)

print(takahashi-aoki)
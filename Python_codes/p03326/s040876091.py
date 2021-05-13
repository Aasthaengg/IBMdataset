N, M = map(int, input().split())
datalist = [list(map(int, input().split())) for _ in range(N)]
tmp = 0

ans1 = []
ans2 = []
ans3 = []
ans4 = []
ans5 = []
ans6 = []
ans7 = []
ans8 = []

for i in range(N):
    tmp = (datalist[i][0] + datalist[i][1] + datalist[i][2])
    ans1.append(tmp)
    tmp = 0
ans1.sort(reverse=True)
ans1 = sum(ans1[:M])
for i in range(N):
    tmp = (datalist[i][0] + datalist[i][1] - datalist[i][2])
    ans2.append(tmp)
    tmp = 0
ans2.sort(reverse=True)
ans2 = sum(ans2[:M])
for i in range(N):
    tmp = (datalist[i][0] - datalist[i][1] + datalist[i][2])
    ans3.append(tmp)
    tmp = 0
ans3.sort(reverse=True)
ans3 = sum(ans3[:M])
for i in range(N):
    tmp = (datalist[i][0] - datalist[i][1] - datalist[i][2])
    ans4.append(tmp)
    tmp = 0
ans4.sort(reverse=True)
ans4 = sum(ans4[:M])
for i in range(N):
    tmp = (-datalist[i][0] + datalist[i][1] + datalist[i][2])
    ans5.append(tmp)
    tmp = 0
ans5.sort(reverse=True)
ans5 = sum(ans5[:M])
for i in range(N):
    tmp = (-datalist[i][0] + datalist[i][1] - datalist[i][2])
    ans6.append(tmp)
    tmp = 0
ans6.sort(reverse=True)
ans6 = sum(ans6[:M])
for i in range(N):
    tmp = (-datalist[i][0] - datalist[i][1] + datalist[i][2])
    ans7.append(tmp)
    tmp = 0
ans7.sort(reverse=True)
ans7 = sum(ans7[:M])
for i in range(N):
    tmp = (-datalist[i][0] - datalist[i][1] - datalist[i][2])
    ans8.append(tmp)
    tmp = 0
ans8.sort(reverse=True)
ans8 = sum(ans8[:M])

ans = max(ans1,ans2,ans3,ans4,ans5,ans6,ans7,ans8)
print(ans)


n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
dis = []
count = 0
for i,j in zip(a,b):
    if j > i:
        ans += 1
        count += j-i
    else:
        dis.append(i-j)
dis.sort(reverse=True)
if count > 0 and dis == []:
    print(-1)
else:
    now = 0
    while now < len(dis) and count > 0:
        ans += 1
        count -= dis[now]
        now += 1
    if count > 0:
        print(-1)
    else:
        print(ans)
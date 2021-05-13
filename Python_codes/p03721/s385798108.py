n,k = map(int,input().split())
AB = []
for i in range(n):
    a,b = map(int,input().split())
    AB.append([a,b])
AB.sort()
ans = 0
cnt = 0
for i in range(n):
    cnt += AB[i][1]
    ans = AB[i][0]
    if cnt >=k:
        print(ans)
        exit()

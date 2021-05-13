n,k = map(int,input().split())
cnt = 0
num = []
for i in range(n):
    a,b = map(int,input().split())
    num.append((a,b))
num.sort()
for i in range(n):
    cnt += num[i][1]
    if cnt >= k:
        print(num[i][0])
        exit()
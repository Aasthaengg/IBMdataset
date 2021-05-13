n = int(input())
lis = [list(map(int,input().split())) for i in range(n)]
lis.sort(key = lambda x:x[1])
lis.sort(key = lambda x:x[0])
ans = 10 ** 8
for i in range(n):
    for j in range(i,n):
        p = lis[j][0]-lis[i][0]
        q = lis[j][1]-lis[i][1]
        li = lis.copy()
        cnt = 0
        while li:
            a = li.pop(0)
            while [a[0]+p,a[1]+q] in li:
                a = li.pop(li.index([a[0]+p,a[1]+q]))
            cnt += 1
        ans = min(ans,cnt)
print(ans)
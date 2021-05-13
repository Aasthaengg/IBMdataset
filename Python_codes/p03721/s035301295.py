n,k = map(int,input().split())
ans = []
for i in range(n):
    a,b = map(int,input().split())
    ans.append([a,b])
ans.sort()
for i in range(len(ans)):
    k = k - ans[i][1]
    if k<=0:
        print(ans[i][0])
        break

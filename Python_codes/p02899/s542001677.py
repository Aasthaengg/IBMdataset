n = int(input())
a = list(map(int, input().split()))
ans = [[] for i in range(n)]
for i in range(n):
    ans[i] = [a[i], i+1]
#print(ans)
ans.sort()
#print(ans)
for i in range(n):
    print(ans[i][1], end=" ")
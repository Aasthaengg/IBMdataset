n = int(input())
ab_ls = [[0,0] for _ in range(n)]
for i in range(n):
    a,b = map(int,input().split())
    ab_ls[i] = [a,b]
ab_ls.sort(reverse=True,key = lambda x:x[0]+x[1])
ans = 0
for i in range(n):
    if i % 2 == 0:
        ans += ab_ls[i][0]
    else:
        ans -= ab_ls[i][1]
print(ans)

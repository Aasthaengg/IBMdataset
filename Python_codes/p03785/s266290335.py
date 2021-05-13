n,c,k = map(int, input().split())
lis  =[int(input()) for _ in range(n)]
lis  =sorted(lis)

ans = 0
tmp = lis[0]
cnt = 0
for i in range(n):
    if tmp+k >= lis[i] and cnt <= c-1:
        cnt += 1
    else:
        ans += 1
        tmp = lis[i]
        cnt = 1

print(ans + 1)

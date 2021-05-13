n = int(input())
a = [int(input()) for i in range(n)]

if a[0] != 0:
    print(-1)
    exit()
inc_cnt = 0
ans = 0
for i in range(n-1):
    if a[i] + 1 < a[i+1]:
        print(-1)
        exit()
    if a[i] + 1 == a[i+1]:
        inc_cnt = a[i+1]
    else:
        ans += inc_cnt
        inc_cnt = a[i+1]
ans += inc_cnt
print(ans)
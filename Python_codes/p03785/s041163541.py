n, c, k = map(int, input().split())
t_lst = [int(input()) for _ in range(n)]
t_lst.sort()
ans = 0
cnt = 0
last = 0
if c == 1:
    print(n)
    exit()
for t in t_lst:
    if t > last:
        ans += 1
        last = t + k
        cnt = 1
    else:
        cnt += 1
        if cnt == c:
            last = 0
            cnt = 0
print(ans)
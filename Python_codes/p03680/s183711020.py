n = int(input())
a = [0]+[int(input()) for _ in range(n)]
check = [0] * (n+1)
now = 1
cnt = 0
while now != 2:
    if check[now] == 1: break
    cnt += 1
    check[now] = 1
    now = a[now]
print(cnt if now == 2 else -1)
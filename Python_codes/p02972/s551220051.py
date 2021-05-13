n = int(input())
a = list(map(int, input().split()))
a = [0] + a
ans = [0] * (n+1)
for i in range(n, 0, -1):
    now = 2 * i
    tmp = 0
    while now <= n:
        tmp += ans[now]
        now += i
    ans[i] = (a[i]-tmp)%2
print(sum(ans))
for i in range(n+1):
    if ans[i] == 1:
        print(i)
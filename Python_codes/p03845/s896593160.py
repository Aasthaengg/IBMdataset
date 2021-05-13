n = int(input())
t = list(map(int, input().split()))
m = int(input())
t_sum = sum(t)

for i in range(m):
    p, x = map(int, input().split())
    ans = t_sum - t[p-1] + x
    print(ans)
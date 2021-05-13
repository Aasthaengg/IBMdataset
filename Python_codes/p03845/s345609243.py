n = int(input())
t = list(map(int, input().split()))
m = int(input())
t_sum = sum(t)
ans = []
for i in range(m):
    t_sum = sum(t)
    p, x = map(int, input().split())
    p -= 1
    t_sum -= t[p]
    t_sum += x
    ans.append(t_sum)
    # print(t_sum)
for i in range(m):
    print(ans[i])

N,M,C = map(int, input().split())
li_b = list(map(int, input().split()))
li_a = []
ans = 0
for i in range(N):
    li = list(map(int, input().split()))
    li_a.append(li)
for i in range(N):
    num_sum = 0
    for t in range(M):
        num_sum += li_a[i][t]*li_b[t]
    if num_sum + C > 0:
        ans += 1
print(ans)
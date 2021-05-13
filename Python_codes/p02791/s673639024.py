N = int(input())
p_list = list(map(int, input().split()))

min_num = N+1
ans = 0

for i in range(N):
    if p_list[i] < min_num:
        ans += 1
        min_num = p_list[i]
print(ans)
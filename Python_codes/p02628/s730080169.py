n, k = map(int, input().split())
p_list = list(map(int, input().split()))

p_list_min = sorted(p_list)
ans = sum(p_list_min[0:k])

print(ans)
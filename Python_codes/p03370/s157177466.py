n, x = map(int, input().split())
m_l = [ int(input()) for _ in range(n) ]
sum_l = sum(m_l)
min_m = min(m_l)
ans = n + int((x-sum_l)/min_m)
print(ans)
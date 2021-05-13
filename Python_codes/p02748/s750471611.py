a, b, m = map(int, input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
m_list = [list(map(int, input().split())) for i in range(m)]

ans = min(a_list) + min(b_list)

for i in range(m):
    ans = min(ans, a_list[m_list[i][0] - 1] + b_list[m_list[i][1] - 1] - m_list[i][2])

print(ans)
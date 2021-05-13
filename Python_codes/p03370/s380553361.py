data = [int(i) for i  in input().split(' ')]
N = data[0]
X = data[1]

m_list = []
for n in range(N):
    m_list.append(int(input()))

X = X - sum(m_list)
div = X//min(m_list)

ans = N + div

print(ans)
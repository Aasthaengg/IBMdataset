n, x = map(int, input().split())
m_list = []
for _ in range(n):
    m_list.append(int(input()))

# print(f"{n} {x}")
# print(m_list)

nokori = x - sum(m_list)
# print(nokori)
sarani = nokori // min(m_list)
# print(sarani)
print(len(m_list) + sarani)
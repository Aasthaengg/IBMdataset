n, x = [int(s) for s in input().split()]
m_list = sorted([int(input()) for _ in range(n)])
print(n + (x - sum(m_list)) // m_list[0])
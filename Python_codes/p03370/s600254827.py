N, X = map(int, input().split())
m_list = [int(input()) for i in range(N)]

Sum = sum(m_list)
Min = min(m_list)
a = (X - Sum) // Min
print(N + a)

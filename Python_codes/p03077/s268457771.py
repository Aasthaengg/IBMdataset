n = int(input())
m = [int(input()) for _ in range(5)]
m_min = min(m)

if n % m_min == 0:
    cost = n // m_min
else:
    cost = n // m_min + 1
print(4 + cost)
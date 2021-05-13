s, t = [input() for _ in range(2)]
max_count = 0
for i in range(len(s) - len(t) + 1):
    m_count = 0
    for j in range(len(t)):
        if s[i+j] == t[j]:
            m_count += 1
    if max_count < m_count:
        max_count = m_count

print(len(t)-max_count)

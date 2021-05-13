N = int(input())
S = input()

pin = []
for i in range(10):
    for j in range(10):
        for k in range(10):
            pin.append(str(i)+str(j)+str(k))

count = 0
for i in range(len(pin)):
    l, m, n = pin[i][0], pin[i][1], pin[i][2]
    l_idx, m_idx, n_idx = -1, -1, -1
    for i in range(N):
        if S[i] == l:
            l_idx = i
            break
    if l_idx != -1:
        for i in range(l_idx+1, N):
            if S[i] == m:
                m_idx = i
                break
    if m_idx != -1:
        for i in range(m_idx+1, N):
            if S[i] == n:
                n_idx = i
                break
    if l_idx != -1 and m_idx != -1 and n_idx != -1:
        count += 1

print(count)
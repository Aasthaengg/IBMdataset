N, K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
M = 10**9 + 7
if N == K:
    result = 1
    for i in range(K):
        result = result * A[i] % M
    print(result)
    exit()
minus = [i for i in A if i <= 0]
l_minus = len(minus)
plus = [i for i in A if i > 0]
l_plus = len(plus)
plus.sort(reverse=1)
minus.sort()
if len(plus) == 0 and K % 2 == 1:
    result = 1
    for i in range(K):
        result = result * minus[-i-1] % M
    print(result)
    exit()

array = []
if K%2 == 1:
    array.append(plus.pop(0))
    l_plus -= 1
    K -= 1
m_x = 0
p_x = 0
max_mm = -1
if (m_x+1) * 2 <= l_minus:
    max_mm = minus[m_x * 2] * minus[m_x * 2 + 1]
max_pp = -1
if (p_x+1) * 2 <= l_plus:
    max_pp = plus[p_x * 2] * plus[p_x * 2 + 1]
counter = 0
\
while counter * 2 + 1 < K:
    if max_pp > max_mm:
        array.append(plus[p_x * 2])
        array.append(plus[p_x * 2 + 1])
        p_x += 1
        if (p_x+1) * 2 <= l_plus:
            max_pp = plus[p_x * 2] * plus[p_x * 2 + 1]
        else:
            max_pp = -1
 
    else:
        array.append(minus[m_x * 2])
        array.append(minus[m_x * 2 + 1])
        m_x += 1
        if (m_x+1) * 2 <= l_minus:
            max_mm = minus[m_x * 2] * minus[m_x * 2 + 1]
        else:
            max_mm = -1
    counter += 1

result = 1
for each in array:
    result = result * each % M
print(result)
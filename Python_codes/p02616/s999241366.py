from collections import deque
n, k = map(int,input().split())
a = list(map(int,input().split()))
mod = 10 ** 9 + 7

p = []
m = []
for i in a:
    if i >= 0:p.append(i)
    elif i < 0:m.append(i)

p.sort(reverse=True)
m.sort()
res = 1
if n == k:
    for i in a:
        res = (res * i) %mod
    print(res)
    exit()
    
if len(p) == 0 and k % 2 == 1:
    for i in range(k):
        res = (res * m[-(i + 1)]) %mod
    print(res)

else:
    p_ind = 0
    m_ind = 0
    while k:
        if k == 1:
            res = (res * p[p_ind]) % mod
            break
        
        temp = p[p_ind] * p[p_ind + 1] if p_ind + 1 < len(p) else 0
        temp1 = m[m_ind] * m[m_ind + 1] if m_ind + 1 < len(m) else 0
        if temp > temp1:
            res = (res * p[p_ind]) %mod
            p_ind += 1
            k -= 1
        else:
            res = (res * temp1) %mod
            m_ind += 2
            k -= 2
    print(res)
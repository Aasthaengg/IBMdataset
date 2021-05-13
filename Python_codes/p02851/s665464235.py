from collections import deque, defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

Si_m_i = [0]
total = 0
temp = 0
for i in range(N):
    total += A[i]
    temp = (total-i-1) % K
    Si_m_i.append(temp)

ret = 0
d = defaultdict(deque)
for i in range(N+1):
    pair = Si_m_i[i]
    temp = d[pair]
    while temp and i-temp[0] >= K:
        temp.popleft()
    ret += len(temp)
    d[Si_m_i[i]].append(i)

print(ret)



import numpy as np

LIM = int(10e5)
time = [0] * (LIM + 1)
N, C = list(map(int, input().split(" ")))
schs = []
for _ in range(N):
    s, t, c = list(map(int, input().split(" ")))
    schs.append((s,t,c))
schs.sort(key = lambda x:x[0])

schs.sort(key = lambda x:x[2])

# print(schs)
for i,temp in enumerate(schs):
    s,t,c = temp

    s_p,t_p,c_p = schs[i-1]
    if i != 0 and c_p == c and t_p == s:
        time[t_p + 1] += 1
        time[t + 1] -= 1

    else:
        time[s] += 1
        time[t + 1] -= 1
# print(time[:100])
ruiseki = np.cumsum(time)

# print(ruiseki[:10])x
print(np.max(ruiseki[1:]))
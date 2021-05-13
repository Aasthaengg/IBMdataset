def actual(N, T, C, t_list):
    if all([t > T for t in t_list]):
        return 'TLE'

    m = 1000

    for c, t in zip(C, t_list):
        if t <= T:
            m = min(m, c)

    return m

N, T = map(int, input().split())

C = []
t_list = []
for _ in range(N):
  c, t = map(int, input().split())
  C.append(c)
  t_list.append(t)

print(actual(N, T, C, t_list))
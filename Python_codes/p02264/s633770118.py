import collections
import sys

p_q = collections.deque(maxlen = 100000)

e_time = 0

n, q = map(int, sys.stdin.readline().split())

for i in range(n):
    p_name, r_time = sys.stdin.readline().split()
    p_q.append([p_name, int(r_time)])

while p_q:
    t_p = p_q.popleft()
    if t_p[1] > q:
        t_p[1] -= q
        e_time += q
        p_q.append(t_p)
    else:
        e_time += t_p[1]
        print(t_p[0], e_time)
import sys

N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))

MOD = 10 ** 9 + 7

t_max = [0] * N
t_min = [1] * N
tmp = -1
for i in range(N):
    t = T[i]
    if t > tmp:
        t_max[i] = t
        t_min[i] = t
    elif t == tmp:
        t_max[i] = t
    else:
        print(0)
        sys.exit(0)
    tmp = t

a_max = [0] * N
a_min = [1] * N
tmp = -1
for i in range(N-1, -1, -1):
    a = A[i]
    if a > tmp:
        a_max[i] = a
        a_min[i] = a
    elif a == tmp:
        a_max[i] = a
    else:
        print(0)
        sys.exit(0)
    tmp = a

answer = 1
for i in range(N):
    tmp = min(t_max[i], a_max[i]) - max(t_min[i], a_min[i])
    if tmp < 0:
        print(0)
        sys.exit(0)
    answer *= tmp + 1
    answer %= MOD

print(answer)

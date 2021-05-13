import sys
def I(): return int(sys.stdin.readline().rstrip())

N = I()
P = [0] + [I() for _ in range(N)]

Q = [0]*(N+1)
for i in range(1,N+1):
    Q[P[i]] = i

# Qの最大連続増加部分列の長さを求める

a = 1
b = 1
for i in range(2,N+1):
    if Q[i] > Q[i-1]:
        b += 1
    else:
        a = max(a,b)
        b = 1
a = max(a,b)

print(N-a)

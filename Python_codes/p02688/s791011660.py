# ABC166
# B Trick or Treat
N, K = map(int, input().split())
A = [list(map(int, input().split())) for i in range(K*2)]
D = list(A[::2])
del A[::2]
A = sum(A, [])
a = set(A)
OP = [n +1 for n in range(N)]
op = set(OP)
an = op - a
print(len(list(an)))

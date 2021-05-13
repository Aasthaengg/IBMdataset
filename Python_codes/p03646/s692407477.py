k = int(input())
N = 50
mk = k%N
qk = k//N
ans = [2*N + qk - mk]*mk + [N + qk - mk - 1]*(N - mk)
print(N)
print(' '.join([str(i) for i in ans]))

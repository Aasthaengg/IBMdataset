import numpy
N = int(input())
p = [i for i in map(float, input().split())]
memo = numpy.zeros([N+1, N+1], dtype = float)
memo[0][0] = 1
for n in range(N):
    memo[n+1] = memo[n]*(1-p[n])
    memo[n+1][1:N+1] += memo[n][0:N] * (p[n])
print(numpy.sum(memo[N][N//2+1:N+1]))
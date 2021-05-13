import numpy
N, K = map(int,input().split())
h = numpy.array(input().split(),dtype=numpy.int64)
dp = numpy.array([0]*N,dtype = numpy.int64)
for i in range(1,N) :
    s = max(0,i-K)
    c = dp[s:i] + numpy.abs(h[i]-h[s:i])
    dp[i] = numpy.min(c)
print(dp[-1])
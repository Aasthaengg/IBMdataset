import scipy.misc
N, M = map(int, input().split())
ansN = 0
ansM = 0
if N != 1:
    ansN = N*(N-1)/2
if M != 1:
    ansM = M*(M-1)/2
ans = int(ansN+ansM)
print(ans)

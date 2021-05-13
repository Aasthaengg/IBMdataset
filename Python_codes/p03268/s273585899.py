from sys import exit, stdin
N, K = [int(_) for _ in stdin.readline().rstrip().split()]
num = [0]*K
for i in range(1, N+1):
    num[i%K]+=1
res = 0
for a in range(K):
    b = (K-a) % K
    c = (K-a) % K
    if ((b+c) % K != 0):
        continue
    res += num[a] * num[b] * num[c]
print(res)
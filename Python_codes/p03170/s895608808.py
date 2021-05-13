N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
m = min(A)
DP = [False] * (K+1)

for i in range(m, K+1):
    for a in A:
        if i - a >= 0 and DP[i-a] == False:
            DP[i] = True
            break
if DP[-1]:
    print('First')
else:
    print('Second')
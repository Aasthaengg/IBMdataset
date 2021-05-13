N, K = map(int, input().split())
A = list(map(int, input().split()))
D = {}
for a in A:
    if a not in D:
        D[a] = 1
    else:
        D[a] += 1

D_list = sorted(D.items(), key=lambda x: x[1])
N = len(D_list)
ANS = 0
for t in D_list:
    if N <= K:
        break
    ANS += t[1]
    N -= 1

print(ANS)



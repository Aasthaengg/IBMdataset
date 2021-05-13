import math

N = int(input())
k = math.ceil((2 * N) ** 0.5)
if N * 2 != k * (k - 1):
    print('No')
else:
    print('Yes')
    print(k)
    S = [[k - 1] for _ in range(k)]
    cnt = 1
    for i in range(k):
        for j in range(i+1, k):
            S[i].append(cnt)
            S[j].append(cnt)
            cnt += 1
    for i in range(k):
        print(" ".join(map(str, S[i])))
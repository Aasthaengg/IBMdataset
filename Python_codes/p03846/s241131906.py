from collections import Counter
N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
MOD = 10 ** 9 + 7
corrct = []
t = N - 1
for i in range(N):
    corrct.append(t)
    if i % 2 == 1:
        t -= 2

if all(corrct[i] == A[i] for i in range(N)):
    print(pow(2, N//2, MOD))
else:
    print(0)

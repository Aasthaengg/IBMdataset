from collections import Counter

N = int(input())
A = list(map(int, input().split()))

B = Counter(A)
Key = list(B.keys())
Key.sort()

M = 10 ** 6
table = [1] * (M + 1)
cnt = 0
for k in Key:
    if B[k] == 1 and table[k] == 1:
        cnt += 1
    
    for i in range(M):
        if k * i > M:
            break
        else:
            table[k * i] = 0
print(cnt)
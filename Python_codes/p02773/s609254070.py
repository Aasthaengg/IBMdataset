from collections import Counter
N = int(input())
S = []
for _ in range(N):
    S.append(input())
S.sort()
C = Counter(S)
C = sorted(C.items(), key=lambda x:x[1], reverse=True)
vm = 0
for k, v in C:
    if v >= vm:
        vm = v
        print(k)
    else:
        break
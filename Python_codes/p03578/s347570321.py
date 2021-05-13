from collections import Counter


N = int(input())
D = Counter(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

for t in T:
    if D[t] - 1 < 0:
        print("NO")
        break
    D[t] -= 1
else:
    print("YES")

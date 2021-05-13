from collections import Counter

N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

Dc = Counter(D)
Tc = Counter(T)

for k, v in Tc.items():
    if Dc[k] < v:
        print("NO")
        break
else:
    print("YES")
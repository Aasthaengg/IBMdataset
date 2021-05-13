from collections import Counter
_ = input()
D = map(int, input().split())
_ = input()
T = Counter(map(int, input().split()))
for d in D:
  if d in T and T[d] > 0:
    T[d] -= 1
print('YES' if all(v==0 for v in T.values()) else 'NO')
import bisect
N, X = map(int, input().split())
L = list(map(int, input().split()))
D = [0]
for l in L:
  D.append(l+D[-1])
print(bisect.bisect_right(D, X))
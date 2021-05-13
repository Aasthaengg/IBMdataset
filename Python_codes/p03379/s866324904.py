# C - Many Medians
# https://atcoder.jp/contests/abc094/tasks/arc095_a

n = int(input())
X = list(map(int, input().split()))

sortedX = sorted(X)

l = sortedX[n // 2 - 1]
r = sortedX[n // 2]

for x in X:
  if x <= l:
    print(r)
  else:
    print(l)
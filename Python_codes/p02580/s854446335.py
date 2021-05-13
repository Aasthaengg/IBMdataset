import sys
input = sys.stdin.buffer.readline
 
H, W, M = map(int, input().split())
 
X = [0] * W
Y = [0] * H
Map = []
 
for _ in range(M):
    h, w = map(int, input().split())
    h -= 1
    w -= 1
    Y[h] += 1
    X[w] += 1
    Map.append((h, w))
 
MX = max(X)
MY = max(Y)
ans = MX + MY
Xans = set()
Yans = set()
for i, x in enumerate(X):
    if x == MX:
        Xans.add(i)
for i, y in enumerate(Y):
    if y == MY:
        Yans.add(i)
cnt = 0
for h, w in Map:
    if h in Yans and w in Xans:
        cnt += 1
if cnt == len(Xans) * len(Yans):
    ans -= 1
print(ans)
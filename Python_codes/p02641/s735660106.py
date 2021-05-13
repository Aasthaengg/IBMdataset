X, N = map(int, input().split())
p = list(map(int, input().split()))

candidates = []

x = X
while(True):
    if not x in p:
        candidates.append(x)
        break
    else:
        x += 1
x = X
while(True):
    if not x in p:
        candidates.append(x)
        break
    else:
        x -= 1

if abs(X-candidates[0]) == abs(X-candidates[1]):
    print(min(candidates))
elif abs(X-candidates[0]) > abs(X-candidates[1]):
    print(candidates[1])
else:
    print(candidates[0])

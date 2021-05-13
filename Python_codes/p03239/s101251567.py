N, T = map(int, input().split())
l = []
for _ in range(N):
    l.append(tuple(map(int, input().split())))

di = dict(l)

keys = [k for k, v in di.items() if v <=T]

if keys:
    print(min(keys))
else:
    print("TLE")
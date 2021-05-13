N = int(input())

x, y = map(int, input().split())
mz = Mz = x + y
mw = Mw = x - y

for i in range(N-1):
    x, y = map(int, input().split())
    z = x + y
    w = x - y
    mz = min(mz, z)
    Mz = max(Mz, z)
    mw = min(mw, w)
    Mw = max(Mw, w)

print(max(Mz-mz, Mw - mw))

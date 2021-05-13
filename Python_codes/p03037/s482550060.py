n ,m = map(int, input().split())
L = []
R = []
for i in range(m):
    l, r = input().split()
    L.append(int(l))
    R.append(int(r))
x = min(R) - max(L) + 1
print(x if x > 0 else "0")
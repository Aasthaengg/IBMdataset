N, M = map(int,input().split())
L = []
R = []
for i in range(M):
    l, r = input().split()
    L.append(int(l))
    R.append(int(r))

if max(L) <= min(R):
    print(min(R) - max(L) + 1)
else:
    print(0)
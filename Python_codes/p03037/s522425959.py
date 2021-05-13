N,M=map(int, input().split())
L = []
R = []
for i in range(M):
    l, r = input().split()
    L.append(int(l))
    R.append(int(r))


x = min(R)-max(L)


print(0 if x <0 else x+1)
N = int(input())

S = set()
for i in range(1,N):
    for j in range(i+1, N+1):
        S.add((i,j))

d = set()
if N % 2 == 0:
    for i in range(1,N//2+1):
        d.add((i, N-i+1))
else:
    for i in range(1,N//2+1):
        d.add((i, N-i))

r = S.difference(d)

print(len(r))
for i in r:
    print(i[0], i[1])


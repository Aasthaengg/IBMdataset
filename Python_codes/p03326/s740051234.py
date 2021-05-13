import itertools
N, M = map(int, input().split())
xyz = list()
for n in range(N):
    xyz.append([int(x) for x in input().split()])
ans = 0
for a,b,c in itertools.product([-1,1], repeat=3):
    tmp = []
    for x, y, z in xyz:
        tmp.append(a*x+b*y+c*z)
    tmp.sort(reverse=True)
    ans = max(ans, sum(tmp[:M]))
print(ans)

import itertools
N = int(input())
xy = []
for _ in range(N):
    x, y = map(int, input().split())
    xy.append([x, y])

cnt = list(itertools.permutations(xy))
ans = []
for c in cnt:
    ky = []
    for n in range(N-1):
        k = ((c[n][0]-c[n+1][0])**2+(c[n][1]-c[n+1][1])**2)**(1/2)
        ky.append(k)
    ans.append(sum(ky))
print(sum(ans)/len(ans))
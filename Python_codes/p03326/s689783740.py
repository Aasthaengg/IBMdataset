N, M = map(int, input().split())
xyz = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for i in range(8):
    tmp = 0
    if i == 0:
        tmp = [x+y+z for x, y, z in xyz]
    if i == 1:
        tmp = [-x+y+z for x, y, z in xyz]
    if i == 2:
        tmp = [x-y+z for x, y, z in xyz]
    if i == 3:
        tmp = [-x-y+z for x, y, z in xyz]
    if i == 4:
        tmp = [x+y-z for x, y, z in xyz]
    if i == 5:
        tmp = [-x+y-z for x, y, z in xyz]
    if i == 6:
        tmp = [x-y-z for x, y, z in xyz]
    if i == 7:
        tmp = [-x-y-z for x, y, z in xyz]
    
    a = 0
    tmp.sort(reverse=True)
    for t in tmp[:M]:
        a += t
    ans = max(ans, a)
print(ans)

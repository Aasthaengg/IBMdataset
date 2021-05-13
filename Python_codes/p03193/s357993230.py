from sys import stdin

n,h,w = [int(x) for x in stdin.readline().rstrip().split()]
li = [list(map(int,stdin.readline().rstrip().split())) for _ in range(n)]
point = 0
for i in li:
    if i[0] >= h and i[1] >= w:
        point += 1
print(point)
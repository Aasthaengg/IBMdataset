from sys import stdin
n,m = map(int,stdin.readline().rstrip().split())
ab = [list(map(int,stdin.readline().rstrip().split())) for _ in range(m)]
li = [0 for _ in range(n+1)]
for a,b in ab:
    li[a] += 1
    li[b] += 1
for i in li:
    if i%2 == 1:
        print("NO")
        exit()
print("YES")
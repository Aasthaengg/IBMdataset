import sys
input = sys.stdin.readline

H,W = list(map(int,input().split()))
t = '.'*(W+2)
camp = [t]
for h in range(H):
    camp.append('.' + input().rstrip() + '.')
camp.append(t)

for h in range(1,H+1):
    for w in range(1,W+1):
        if camp[h][w] == '#':
            if camp[h][w-1] != '#' and camp[h][w+1] != '#' and camp[h-1][w] != '#' and camp[h+1][w] != '#':
                print('No')
                exit()
print('Yes')

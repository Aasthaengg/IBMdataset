from sys import stdin
def input():
    return stdin.readline().strip()

n, k = map(int, input().split())
xy  = []
for _ in range(n):
    i, j = map(int, input().split())
    xy.append((i, j))

xy.sort()

# decide left, right, down
ans = float('inf')
for left in range(n-k+1):
    for right in range(left+k-1, n):
        choose = sorted(xy[left:right+1], key=lambda x: x[1])
        for down in range(len(choose)-k+1):
            area = (xy[right][0] - xy[left][0]) * (choose[down+k-1][1] - choose[down][1])
            if area < ans:
                ans = area

print(ans)
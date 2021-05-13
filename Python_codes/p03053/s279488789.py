import sys
from collections import deque
input = sys.stdin.readline

def main():
    h, w = map(int, input().split())

    a = [input()[:-1] for i in range(h)]

    already = [[False]*w for i in range(h)]
    key = deque([])
    for i in range(h):
        for j in range(w):
            if a[i][j] == '#':
                if not key:
                    judge = (i, j)
                key.append((i, j))
                already[i][j] = True
    
    ans = -1
    way = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    change = False
    while key:
        value = key.popleft()
        if value == judge:
            ans += 1
            judge = value
            change = True
        i, j = value
        for x, y in way:
            p, q = i+x, j+y
            if 0 <= p < h and 0 <= q < w  and not already[p][q]:
                already[p][q] = True
                key.append((p, q))
                if change:
                    judge = (p, q)
                    change = False

    print(ans)







    
if __name__ == "__main__":
    main()


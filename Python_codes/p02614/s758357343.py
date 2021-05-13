from itertools import product

h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]

ans = 0

for row_bit in product(range(2), repeat=h):
    for col_bit in product(range(2), repeat=w):
        cnt = 0
        for row in range(h):
            for col in range(w):
                if c[row][col] == '#' and (row_bit[row] and col_bit[col]):
                    cnt += 1
        if cnt == k:
            ans += 1

print(ans)
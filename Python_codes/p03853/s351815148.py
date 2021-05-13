# https://atcoder.jp/contests/abc049/tasks/abc049_b

h, w = map(int, input().split())
matrix = []
for _ in range(h):
    row = list(input())
    matrix.append(row)
    matrix.append(row)

for m in matrix:
    print(''.join(m))
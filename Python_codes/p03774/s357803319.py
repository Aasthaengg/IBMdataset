n, m = map(int, input().split())

ab = [tuple(map(int, input().split())) for _ in range(n)]
cd = [tuple(map(int, input().split())) for _ in range(m)]

def meter(a, b, c, d):
    return abs(a-c) + abs(b-d)

ans = []

for a, b in ab:
    best_ind = None
    best_dist = float('inf')
    for j, (c, d) in enumerate(cd):
        tmp_dist = meter(a, b, c, d)
#         print(f'{a=}, {b=}, {c=}, {d=}, {tmp_dist=}, {j=}')
        if tmp_dist < best_dist:
#             print('update')
            best_dist = tmp_dist
            best_ind = j+1
    print(best_ind)
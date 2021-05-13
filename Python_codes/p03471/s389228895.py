n, y = map(int, input().split())
discov_flg = False

for a in range(0, n + 1):
    for b in range(0, n + 1 - a):
        c = n - a - b
        total = 10000 * a + 5000 * b + 1000 * c
        if y == total:
            print(f"{a} {b} {c}")
            discov_flg = True
            break
    if discov_flg:
        break
        
if not(discov_flg):
    print("-1 -1 -1")
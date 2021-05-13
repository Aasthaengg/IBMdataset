n, m = map(int, input().split())
alst = [input() for _ in range(n)]
blst = [input() for _ in range(m)]

for i in range(n - m + 1):
    for j in range(n - m + 1):
        for k, row in enumerate(blst):
            if alst[i + k][j:j + m] == blst[k]:
                continue
            break
        else:
            print("Yes")
            exit()
print("No")
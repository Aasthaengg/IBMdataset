N, K = map(int, input().split())
if K >= N:
    print(0)
    exit()
H = sorted(list(map(int, input().split())))
print(sum(H[0: N - K]))
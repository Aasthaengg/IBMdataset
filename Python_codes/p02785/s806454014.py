N, K = map(int, input().split())
H = sorted(list(map(int, input().split())))

print(sum(H[:-K] if K != 0 else H))

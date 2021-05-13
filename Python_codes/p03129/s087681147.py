N, K = map(int, input().split())

print(["YES", "NO"][not(K <= ((N + 1) // 2))])

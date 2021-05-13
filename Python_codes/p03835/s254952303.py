k, s = map(int, input().split())

print(sum(0 <= s - x - y <= k for x in range(k+1) for y in range(k+1)))
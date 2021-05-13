H1, M1, H2, M2, K = map(int, input().split())

start = 60 * H1 + M1
end = 60 * H2 + M2

print((end - K) - start)

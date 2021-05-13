H1, M1, H2, M2, K = map(int, input().split())
time1 = H1 * 60 + M1
time2 = H2 * 60 + M2

print(max(0, time2 - time1 - K))
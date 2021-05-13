h1, m1, h2, m2, k = map(int, input().split())
time1 = h1 * 60 + m1
time2 = h2 * 60 + m2
print(max(time2 - k - time1, 0))
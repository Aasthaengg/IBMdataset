h1, m1, h2, m2, k = map(int, input().split())

hour = h2 - h1
minute = m2 - m1
time = (hour * 60) + minute

print(time - k)

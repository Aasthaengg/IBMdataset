h1, m1, h2, m2, k = map(int, input().split())

difh = h2 - h1
difm = m2 - m1

t = 60 * difh + difm

print(max(0, t - k))
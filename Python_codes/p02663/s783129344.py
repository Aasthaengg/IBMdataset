h1, m1, h2, m2, k = map(int, input().split())

deltaH = h2 - h1
deltaM = m2 - m1
delta = deltaH * 60 + deltaM - k

print(delta)

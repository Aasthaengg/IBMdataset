import math
a, b, h, m = map(int, input().split())

pi = math.pi

m_rad = 2 * pi * m / 60
h_rad = 2 * pi * h / 12 + 2 * pi / 12 * m / 60

"""
余弦定理： sqrt(a^2 + b^2 - 2abcosΘ)
cos(-Θ) = cos(Θ)
cos(2pi - Θ) = cos(Θ) 
"""

ans = math.sqrt(a * a + b * b - 2 * a * b * math.cos(m_rad - h_rad))
print("{:.12f}".format(ans))
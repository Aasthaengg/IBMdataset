import numpy as np

a, b, h, m = map(int,input().split())

beta = 2*np.pi / 60 * float(m)
alpha = 2*np.pi / 12 * h + 2*np.pi /12 /60 * m
theta = abs(alpha - beta)

ans = np.sqrt((a - b*np.cos(theta))**2 + (b*np.sin(theta))**2)

print(ans)
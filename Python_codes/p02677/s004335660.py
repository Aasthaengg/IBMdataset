import numpy as np

A, B, H, M = map(int, input().split())


angle_h = 1./ 12.*(H + M/60.) * 2*np.pi

angle_m = M/60. * 2 * np.pi

hour = (A*np.sin(angle_h), A*np.cos(angle_h))
minute = (B*np.sin(angle_m), B*np.cos(angle_m))

dist = np.sqrt((hour[0] - minute[0])**2 + (hour[1] - minute[1])**2)

print(dist)

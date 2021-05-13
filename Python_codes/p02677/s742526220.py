import math
import numpy as np

A, B, H, M = map(int,input().split())
long = np.array([A*math.sin(H/12*2*math.pi+M/60*math.pi/6), A*math.cos(H/12*2*math.pi+M/60*math.pi/6)])
short = np.array([B*math.sin(M/60*2*math.pi), B*math.cos(M/60*2*math.pi)])

print(np.linalg.norm(long-short))

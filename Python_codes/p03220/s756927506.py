import numpy as np
n = int(input())
t,a = map(int,input().split())
h = np.array([int(i) for i in input().split()])

h_temp = t - h * 0.006
ans = np.abs(h_temp - a).argmin()
print(ans+1)
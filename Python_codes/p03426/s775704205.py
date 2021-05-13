import numpy as np
import sys
input = sys.stdin.readline
h, w, d = map(int, input().split())
num = h * w
mass = np.array([(0, 0) for _ in range(num + 1)])
mp = np.zeros(num+1)
for i in range(1, h+1):
    for j, a in enumerate(map(int, input().split())):
        mass[a] = [i, j+1]
for i in range(d+1, num+1):
    mp[i] = mp[i-d] + np.sum(abs(mass[i]-mass[i-d]))
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(int(mp[r]-mp[l]))

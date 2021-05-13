import sys
input = sys.stdin.readline
h, w, d = map(int, input().split())
num = h * w
x = [0] * (num + 1)
y = [0] * (num + 1)
mp = [0] * (num + 1)
for i in range(h):
    for j, a in enumerate(map(int, input().split())):
        x[a], y[a] = [i+1, j+1]
for i in range(d+1, num+1):
    mp[i] = mp[i-d] + abs(x[i] - x[i-d]) + abs(y[i] - y[i-d])
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(mp[r]-mp[l])


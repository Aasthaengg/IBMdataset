# -*- coding: utf-8 -*-
import copy

a,b = map(int, raw_input().split())
h_max = 40
w_max = 100
ans = []
buff = [ "." for i in range(w_max)]
buff2 = [ "#" for i in range(w_max)]
for j in range(h_max/2):
    tmp = copy.deepcopy(buff)
    ans.append(tmp)
for j in range(h_max/2):
    tmp = copy.deepcopy(buff2)
    ans.append(tmp)

h = h_max
w = w_max
a = a - 1
b = b - 1

px = 0
py = 0
while b > 0:
    b = b - 1
    ans[py][px] = "#"
    px = px + 2
    if px > w_max - 1:
        py = py + 2
        px = 0
#    print("[{} {}]".format(px, py))

px = 0
py = h_max / 2 + 1
while a > 0:
    a = a - 1
    ans[py][px] = "."
    px = px + 2
    if px > w_max - 1:
        py = py + 2
        px = 0
#    print("[{} {}]".format(px, py))

print("{} {}".format(h, w))
for j in range(h):
    print ''.join(ans[j])


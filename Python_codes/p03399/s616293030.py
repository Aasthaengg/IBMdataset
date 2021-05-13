# coding: utf-8
# Your code here!
L  = []
for i in range(4):
    L.append(int(input()))

ans = min(L[0],L[1]) + min(L[2],L[3])
print(ans)
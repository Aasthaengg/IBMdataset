n = int(input())

xl = [0]*n
yl = [0]*n
hl = [0]*n


for i in range(n):
    xl[i], yl[i], hl[i] = map(int, input().split())
    if hl[i] >= 1:
        si = i

ansx, ansy, ansh = -1, -1, -1

for cx in range(101):
    for cy in range(101):
        H = hl[si]+abs(xl[si]-cx)+abs(yl[si]-cy)
        flag = True
        for i in range(n):
            hi = max(H-abs(xl[i]-cx)-abs(yl[i]-cy), 0)
            if hi != hl[i]:
                flag = False
                break
        if flag:
            ansx, ansy, ansh = cx, cy, H
print(ansx, ansy, ansh)

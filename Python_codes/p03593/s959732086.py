import collections

H, W = map(int, input().split())
A = []
for _ in range(H):
    A += list(input())
elements = collections.Counter([x % 4 for x in collections.Counter(A).values()])
c = [0]*4
for x in elements.keys():
    c[x] = elements[x]

ans = False
if H % 2 == 0 and W % 2 == 0:
    if c[1:] == [0, 0, 0]:
        ans = True

elif H % 2 != 0 and W % 2 != 0:
    if c[1] + c[3] == 1:
        if c[1] == 1:
            c[0] += 1
            c[1] = 0
        else:
            c[2] += 1
            c[3] = 0

        if c[1:] == [0, 0, 0] or c[2] <= (H + W)//2 - 1:
            ans = True 

elif H % 2 != 0:
    if c[1:] == [0, 0, 0] or (c[2] <= W//2 and c[1] + c[3] == 0):
        ans = True
else:
    if c[1:] == [0, 0, 0] or (c[2] <= H//2 and c[1] + c[3] == 0):
        ans = True

if ans:
    print('Yes')
else:
    print('No')
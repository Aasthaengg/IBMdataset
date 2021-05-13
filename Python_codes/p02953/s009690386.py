N = int(input())
H = list(map(int,input().split()))

down = False
p = -1
for h in H:
    if p - h >= 2:
        print('No')
        exit()
    if down and p - h >= 1:
        print('No')
        exit()
    if p < h:
        down = False
    elif p > h:
        down = True
    p = h
print('Yes')
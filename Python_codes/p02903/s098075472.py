H, W, A, B = map(int, input().split())

ans = []

for i in range(B):
    lst = [1]*A + [0] *(W-A)
    print(*lst, sep='')
for i in range(H-B):
    lst = [0]*A + [1] *(W-A)
    print(*lst, sep='')

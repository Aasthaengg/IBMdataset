a = []
while True:
    d = list(map(int,input().split()))
    if d == [0,0]:
        break
    a.append(d)
for H,W in a:
    for i in range(0,H):
        print('#'*W)
    print('')
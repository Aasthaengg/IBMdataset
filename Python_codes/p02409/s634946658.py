data = [[[0 for i in range(10)] for j in range(3)] for h in range(4)]
n = int(input())
for o in range(n):
    a = input().split()
    b = int(a[0])
    f = int(a[1])
    r = int(a[2])
    v = int(a[3])
    data[b - 1][f - 1][r - 1] += v

for b in range(4):
    for f in range(3):
        for r in range(10):
            print('',data[b][f][r],end='')
        print()
    if b<3:
        print('#'*20)
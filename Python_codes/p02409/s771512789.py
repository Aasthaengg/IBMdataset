l = [[['0' for i in range(10)] for j in range(3)] for j in range(4)]
for n in range(int(input())):
    b, f, r, v = map(int, input().strip().split())
    l[b-1][f-1][r-1] = str(v + int(l[b-1][f-1][r-1]))
for k in range(4):
    if bool(k):
        print('#'*20)
    for j in l[k]:
        print(' ' + ' '.join(j))
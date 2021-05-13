num = {
    1:{1:[0]*10,2:[0]*10,3:[0]*10},
    2:{1:[0]*10,2:[0]*10,3:[0]*10},
    3:{1:[0]*10,2:[0]*10,3:[0]*10},
    4:{1:[0]*10,2:[0]*10,3:[0]*10}
}

n = int(input())
for _ in range(n):
    b, f, r, v = map(int, input().split())
    num[b][f][r-1] += v
for b in num:
    for f in num[b]:
        for r in num[b][f]:
            print(' '+str(r), end='')
        print()
    if b==4: break
    print('#'*20)


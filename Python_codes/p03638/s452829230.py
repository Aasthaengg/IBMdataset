h,w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
nn = h*w
pos = 0
cnt = 0
while True:
    tmp = []
    for j in range(w):
        if a[pos] == 0:
            pos += 1
        tmp.append(pos+1)
        a[pos] -= 1
    print(*tmp)
    cnt += w
    if cnt >= nn:
        break
    tmp = []
    for j in range(w):
        if a[pos] == 0:
            pos += 1
        tmp.append(pos+1)
        a[pos] -= 1
    print(*tmp[::-1])
    cnt += w
    if cnt >= nn:
        break


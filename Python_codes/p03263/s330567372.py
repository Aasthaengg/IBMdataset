h, w = map(int, input().split())
area = [list(map(int, input().split())) for i in range(h)]

ans = []
temp = []
p = 0
for i in range(h):
    if i%2 == 0:
        rw = list(range(w))
    else:
        rw = list(range(w))[::-1]
    for j in rw:
        if p == 1:
            temp.append('{} {} {} {}'.format(
                prev[0], prev[1], i+1, j+1
            ))
            prev = (i+1, j+1)
        if area[i][j]%2 == 1:
            if p == 0:
                prev = (i+1, j+1)
                p+=1
            elif p == 1:
                p = 0
                ans += temp
                temp = []

print(len(ans))
for a in ans:
    print(a)

n = int(input())
l = [list(map(int, input().split())) for i in range(n)]

sortthird = lambda x: x[2]
l.sort(key = sortthird)

for i in range(101):
    for j in range(101):
        ref = l[-1][2] + abs(l[-1][0] - i) + abs (l[-1][1] - j)
        for k in range(n):
            if l[k][2] == max(0, ref - abs(l[k][0] - i) - abs (l[k][1] - j)):
                continue
            else:
                break
        else:
            print(i, j, ref)
            exit()
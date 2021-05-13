h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))

colored = [[0]*w for _ in range(h)]

color = 0
for ai in a:
    color += 1
    count = 0
    for i in range(w):
        for j in range(h):
            if i % 2 == 0:
                if colored[j][i] == 0:
                    colored[j][i] = color
                    count += 1
                    if count == ai:
                        break
            else:
                if colored[h-1-j][i] == 0:
                    colored[h-1-j][i] = color
                    count += 1
                    if count == ai:
                        break
        else:
            continue
        break
#print(colored)
for i in range(h):
    print(*colored[i])
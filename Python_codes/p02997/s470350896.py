n, k = map(int, input().split())
m = 0
e = []
for i in range(n-1):
    e.append((1, i+2))
    m += 1

rep = (n-1)*(n-2)//2 - k
if rep < 0:
    print(-1)
    exit()
e_list = []
for i in range(2, n+1):
    for j in range(i+1, n+1):
        if rep == 0:
            print(m)
            for edge in e:
                print(*edge)
            exit()
        e.append((i, j))
        m += 1
        rep -= 1

if rep == 0:
    print(m)
    for edge in e:
        print(*edge)






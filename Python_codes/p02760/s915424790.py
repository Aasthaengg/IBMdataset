def check(a):
    m = [-1, -1, -1]
    if [a[0][0], a[1][1],a[2][2]] == m:
        print("Yes")
        return
    if [a[0][2], a[1][1], a[2][0]] == m:
        print("Yes")
        return
    for i in range(3):
        if a[i] == m:
            print("Yes")
            return
        elif [r[i] for r in a] == m:
            print("Yes")
            return
    print("No")
    return

a=[list(map(int,input().split()))for _ in range(3)]
n=int(input())
b=[int(input()) for _ in range(n)]
for i in range(n):
    for y,row in enumerate(a):
        try:
            x=row.index(b[i])
            a[y][x]=-1
        except ValueError:
            pass
check(a)
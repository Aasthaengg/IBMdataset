import sys

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))

c = []
for _ in range(3):
    c.append(LI())
a1_range = min(c[0])
for a1 in range(a1_range+1):
    a = [0]*3
    b = [0]*3
    a[0] = a1
    b[0] = c[0][0] - a[0]
    b[1] = c[0][1] - a[0]
    b[2] = c[0][2] - a[0]
    a[1] = c[1][0] - b[0]
    a[2] = c[2][0] - b[0]
    flag = True
    for i in range(3):
        for j in range(3):
            if c[i][j] != a[i] + b[j]:
                flag = False
                break
        if not flag:
            break
    if flag:
        print("Yes")
        sys.exit()
print("No")
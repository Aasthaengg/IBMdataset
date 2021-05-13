import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n,m = map(int, input().split())
v = [list(map(int, input().split())) for _ in range(m)]

for i in range(1000):
    flag = True
    num = str(i)
    for sc in v:
        if len(num) >= sc[0] and str(sc[1]) == num[sc[0] - 1]:
            continue
        else:
            flag = False
            break
    if flag and len(num) == n:
        print(i)
        exit()
print(-1)

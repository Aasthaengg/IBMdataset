n, m = map(int, input().split())

ab = []
for _ in range(n):
    ab.append(list(map(int, input().split())))

cd = []
for _ in range(m):
    cd.append(list(map(int, input().split())))

tmp = []
for i in range(n):
    ans = 10**9 +7
    ta = 0
    for j in range(m):
        x  = abs(ab[i][0] - cd[j][0])
        y =  abs(ab[i][1] - cd[j][1])
        if ans > x+y:
            ans = x+y
            ta = j+1
    print(ta)
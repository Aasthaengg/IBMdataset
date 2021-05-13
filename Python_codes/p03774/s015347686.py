#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]


n,m = map(int, input().split())
g = [list(map(int,input().split())) for i in range(n)]
c = [list(map(int,input().split())) for i in range(m)]

total = []
for i in range(n):
    temp = []
    for j in range(m):
        distance = abs(g[i][0] - c[j][0]) + abs(g[i][1] - c[j][1])
        temp.append(distance)
    total.append(temp)

#print(total)
for i in range(n):
    midx = 0
    mv = 99999999999999999999999999
    for j in range(m):
        if (mv > total[i][j]):
            midx = j
            mv = total[i][j]
    print(midx+1)

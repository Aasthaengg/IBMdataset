n = int(input())
l = [list(map(int,input().split())) for i in range(n)]
c = 0
for i in range(n):
    c += l[i][1] - l[i][0] + 1

print(c)
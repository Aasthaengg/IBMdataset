n = int(input())
ls = [[int(_) for _ in input().split()] for _ in range(n)]

lsmx = [0, 0]

for i in range(n):
    if ls[i][0] >= lsmx[0]:
        lsmx = ls[i]

print(lsmx[0] + lsmx[1])
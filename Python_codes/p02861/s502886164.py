import itertools
n = int(input())
seq = [i for i in range(n)]
steps = list(itertools.permutations(seq))
xy = [list(map(int,input().split())) for _ in range(n)]
sumlen = 0
for j in range(len(steps)):
    leng = 0
    step = steps[j]
    for k in range(n-1):
        x_1 = int(xy[step[k]][0])
        x_2 = int(xy[step[k+1]][0])
        y_1 = int(xy[step[k]][1])
        y_2 = int(xy[step[k+1]][1])
        leng += ((x_1 - x_2)**2  + (y_1 - y_2)**2)**0.5
    sumlen += leng
print((sumlen/len(steps)))
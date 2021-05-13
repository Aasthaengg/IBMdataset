lst = [[[0 for i in range(10)]for j in range(3)]for k in range(4)]
n = int(input())
for i in range(n):
    b,f,r,v = map(int,raw_input().split())
    lst[b-1][f-1][r-1] += v
for i in range(4):
    if i != 0:
        print "#"*20
    for j in range(3):
        pri = ""
        for k in range(10):
            pri += " "+ str(lst[i][j][k])
        print pri
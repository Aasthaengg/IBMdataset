#coding:utf-8

n = int(input().rstrip())
tatemono=[
[[0 for i in range(10)],[0 for i in range(10)],[0 for i in range(10)]],
[[0 for i in range(10)],[0 for i in range(10)],[0 for i in range(10)]],
[[0 for i in range(10)],[0 for i in range(10)],[0 for i in range(10)]],
[[0 for i in range(10)],[0 for i in range(10)],[0 for i in range(10)]]]

for i in range(n):
    b,f,r,v = [int(i) for i in input().rstrip().split(" ")]
    tatemono[b-1][f-1][r-1] += v

for i in range(3):
    for j in range(3):
        print(" " + " ".join(list(map(str, tatemono[i][j]))))

    print("####################")

for i in range(3):
    print(" " + " ".join(list(map(str, tatemono[3][i]))))
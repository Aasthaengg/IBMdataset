import sys
n=int(input())
a=[[[0 for i in range(10)] for i in range(3)] for i in range(4)]
for i in range(n):
    w=input().split()
    b=(int(w[0]))
    f=(int(w[1]))
    r=(int(w[2]))
    v=(int(w[3]))
    a[b-1][f-1][r-1]+=v
for i in range(4):
    for j in range(3):
        for k in range(10):
            sys.stdout.write(" {0}".format(a[i][j][k]))
        sys.stdout.write("\n")
    if (i!=3):
        for x in range(20):
            sys.stdout.write("#")
        sys.stdout.write("\n")
n = int(raw_input())
l = [[[0 for i in range(10)]for j in range(3)]for k in range(4)]
for i in range(n):
    b,f,r,v = map(int,raw_input().split())
    l[b-1][f-1][r-1] += v
for i in range(4):
    if i != 0:
        print "####################"
    for j in range(3):
        print "",
        for k in range(9):
            print "%d" %l[i][j][k] ,
        print l[i][j][9]
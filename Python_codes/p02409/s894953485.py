list = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]
n = int(input())
for i in range(n):
    b, f, r, v = map(int, input().split())
    list[b-1][f-1][r-1] += v
 
for k in range(4):
    for j in range(3):
        for i in range(10):
            print ("", end=" ")
            print (list[k][j][i], end = "")
        print("")
    if k != 3:
        print("####################")

l = [[0 for i in range(13)] for j in range(4)]
n = int(input())

g = {0:"S",1:"H",2:"C",3:"D"}
h = {"S":0, "H":1, "C":2, "D":3}

for i in range(n):
    s,r = input().split()
    l[h[s]][int(r)-1] = 1

for i in range(4):
    for j in range(13):
        if l[i][j] == 0:
            print(g[i],j+1)
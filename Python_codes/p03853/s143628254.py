from sys import exit

ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

h,w = mi()
cs = [input() for i in range(h)]

for i in range(h):
    for k in range(2):
        for j in range(w):
            print(cs[i][j],end="")
        print("")
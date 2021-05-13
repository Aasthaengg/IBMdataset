from sys import exit

ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

h,w = mi()
a = [input() for i in range(h)]

print("#"*(w+2))

for i in range(h):
    print("#",end="")
    for j in range(w):
        print(a[i][j],end="")
    print("#")
print("#"*(w+2))

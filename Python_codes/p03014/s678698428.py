import sys
def input():
    return sys.stdin.readline()[:-1]
sys.setrecursionlimit(1000000)

h,w=map(int,input().split())
maze = [[]for _ in range(h)]
for i in range(h):
    maze[i].extend(list(input()))

R=[[0 for i in range(w)]for i in range(h)]
L=[[0 for i in range(w)]for i in range(h)]
U=[[0 for i in range(w)]for i in range(h)]
B=[[0 for i in range(w)]for i in range(h)]

for i in range(h):
    for j in range(w):
        if maze[i][j]=="#":continue
        if j==0: L[i][j]=1
        else: L[i][j]=L[i][j-1]+1
        if i==0: U[i][j]=1
        else: U[i][j]=U[i-1][j]+1

for i in range(h):
    for j in range(w):
        if maze[h-1-i][w-1-j]=="#":continue
        if i==0:B[h-1-i][w-1-j]=1
        else: B[h-1-i][w-1-j] = B[h-i][w-1-j]+1
        if j==0:R[h-1-i][w-1-j]=1
        else: R[h-1-i][w-1-j] = R[h-1-i][w-j]+1


#print(*B,sep="\n")
#print("\n")
#print(*U,sep="\n")


ma=0
for i in range(h):
    for j in range(w):
        if maze[i][j]=="#":continue
        ma=max(ma,R[i][j]+L[i][j]+U[i][j]+B[i][j]-3)

print(ma)

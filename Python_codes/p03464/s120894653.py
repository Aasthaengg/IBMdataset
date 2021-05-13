import sys,math,collections,itertools
input = sys.stdin.readline

K=int(input())
A=list(map(int,input().split()))

min_child = 2
max_child = 2

for i in range(K-1,-1,-1):
    if math.ceil(min_child/A[i])>0 and math.floor(max_child/A[i])>0 and math.floor(max_child/A[i])-math.ceil(min_child/A[i])>=0:
        min_child = math.ceil(min_child/A[i])*A[i]
        max_child =math.floor(max_child/A[i])*A[i]+A[i]-1
    else:
        print(-1)
        exit()
print(min_child,max_child)

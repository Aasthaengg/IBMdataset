import sys,math,collections,itertools,bisect
input = sys.stdin.readline

N=int(input())
A=sorted(list(map(int,input().split())))
process = []
for i in range(N-2):
    tmp = A.pop()
    y=A.pop()
    A.append(tmp)
    if y>=0:
        process.append([A[0],y])
        A[0]-=y
    else:
        process.append([A[-1],y])
        A[-1]-=y
process.append([A[-1],A[0]])
print(A[-1]-A[0])
for pro in process:
    print(*pro)

N=int(input())
L=[]
for i in range(N):
    x,l=map(int,input().split())
    a,b=x-l,x+l
    L.append((a,b))
L.sort(key=lambda  ab: ab[1])
#print(L)
robot=1
b=L[0][1]
for i in range(1,N):
    A,B=L[i]
    if A>=b:
        robot+=1
        b=B
print(robot)


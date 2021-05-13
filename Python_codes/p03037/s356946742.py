r=input().split()
N=int(r[0])
M=int(r[1])
data=[[int(s) for s in input().split()] for i in range(M)]
left=[]
right=[]
for i in range(M):
    left.append(data[i][0])
    right.append(data[i][1])
if min(right)-max(left)+1<=0:
    print(0)
else:
    print(min(right)-max(left)+1)
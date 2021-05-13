A,B,M=map(int,input().split())
a_1=list(map(int,input().split()))
b_1=list(map(int,input().split()))
L=[list(map(int,input().split())) for _ in range(M)]

count=[]
count.append(min(a_1)+min(b_1))

for k in range(M):
    count.append(a_1[L[k][0]-1]+b_1[L[k][1]-1]-L[k][2])

print(min(count))
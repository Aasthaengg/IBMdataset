n=int(input())
A=[[i*(i+1)//2,i] for i in range(1,4473)]

point=[]
for i in range(len(A)-1):
    if A[i][0]<=n<=A[i+1][0]:
        point=A[i+1]
        break

num=point[0]-n
for i in range(1,point[1]+1):
    if i==num:continue
    else:print(i)
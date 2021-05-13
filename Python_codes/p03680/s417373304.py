N=int(input())
A=[]
ans=-1
for i in range(N):
    A.append(int(input()))

num=A[0]
for j in range(N):
    if num==2:
        ans=j+1
        break
    num=A[num-1]
print(ans)
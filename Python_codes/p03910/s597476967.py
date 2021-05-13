N=int(input())

sums=0
A=[]
i=1
while sums<N:
    sums+=i
    A.append(i)
    i+=1

cnt=sum(A)-N
for i in A:
    if i!=cnt:
        print(i)
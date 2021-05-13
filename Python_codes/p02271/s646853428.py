n=int(input())
A=list(map(int,input().split()))
q=int(input())
m=list(map(int,input().split()))

sumlist=[]

for i in range(2**n):
    sumA=0
    for j in range(n):
        if ((i>>j) & 1):
            sumA+=A[j]
    sumlist.append(sumA)

for k in range(q):
    if m[k] in sumlist:
        print("yes")
    else:
        print("no")

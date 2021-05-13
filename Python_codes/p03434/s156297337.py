n=int(input())
a=list(map(int,input().split()))
a.sort()

A=[]
B=[]

for i in range(len(a)):
    if i%2==1:
        A.append(a[i])
    else:
        B.append(a[i])

print(abs(sum(A)-sum(B)))
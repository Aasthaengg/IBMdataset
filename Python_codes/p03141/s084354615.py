N=int(input())
A=[0]*N
B=[0]*N
C=[0]*N
for i in range(N):
    a, b = map(int,input().split())
    A[i], B[i], C[i] = a, b, a+b

index = sorted(range(len(C)), key=lambda k: C[k], reverse=True)

sum_=0
for i,idx in enumerate(index):
    if i % 2 ==0:
        sum_+=A[idx]
    else:
        sum_-=B[idx]

print(sum_)
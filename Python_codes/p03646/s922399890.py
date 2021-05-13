# coding: utf-8
# Your code here!
K=int(input())


alpha=K//50
beta=K%50
#print(alpha,beta)

N=50
A=[49+alpha-beta]*N
for i in range(beta):
    A[i]+=51

print(N)
print(*A)

"""
count=0
for i in range(50):
    if A[i]<50:
        continue
    count+=1
    for j in range(50):
        if i==j:
            A[j]-=N
        else:
            A[j]+=1

print(A)
print(count)
"""

[N,M,X] = list(map(int,input().split()))
A = list(map(int,input().split()))

dammy = [0]*(N+1)

for i in A:
    dammy[i]=1
    if i==X:
        dammy[i]=0
# print(dammy)


left = sum(dammy[0:X+1])
right = sum(dammy[X+1:N+1])
# print(left,right)

print(min(left,right))


N = int(input())
[D,X] = list(map(int,input().split()))
A = []
for i in range(N):
    A.append(int(input()))

out=0
for i in range(N):
    j=0
    dam=0
    while True:
        dam = 1 + A[i]*j
        if dam > D:
            break
        out+=1
        j+=1
    # print(i,out)

print(X + out)

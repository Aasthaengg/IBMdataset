n = int(input())
A = list(map(int,input().split()))
q = int(input())
m = list(map(int,input().split()))

cand = []
for i in range(2**n):
    tmp = 0
    for j in range(n):
        if (i>>j)&1:
            tmp += A[j]
    cand.append(tmp)

for i in m:
    if i in cand:
        print("yes")
    else:
        print("no")   

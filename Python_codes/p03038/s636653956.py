import collections

N, M = map(int,input().split())

A = list(map(int,input().split()))
A.sort()
op = [0]*M

for i in range(M):
    b,c = map(int,input().split())
    op[i] = (c, b)

op.sort(reverse=True)

now = 0
flag = False
for i in range(M):
    if flag:
        break
    val, maisu = op[i]
    if now >= N:
        break
    if A[now] < val:
        for j in range(maisu):
            if now+j < N:
                if A[now+j] < val:
                    A[now+j] = val
                else:
                    flag = True
                    break
        now += maisu 
    else:
        break
    
print(sum(A))
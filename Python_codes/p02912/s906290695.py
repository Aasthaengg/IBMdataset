N, M = list(map(int,input().split()))
A = sorted(list(map(int,input().split())), reverse=True)
b = []

b.append(A.pop(0)//2)
for i in range(1,M):
    if A == []:
        b.append(b.pop(0)//2)
    else:
        if A[0] > b[0]:
            b.append(A.pop(0)//2)
        else:
            b.append(b.pop(0)//2)

print(sum(A)+sum(b))
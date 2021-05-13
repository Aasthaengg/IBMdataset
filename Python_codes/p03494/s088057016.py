N = int(input())
A = input().split()
l=list()
for i in range(N):
    A[i] = int(A[i])
    if A[i] % 2 == 1:
        l.append(0)
        break
    else:
        for j in range(30):
            A[i] = A[i] / 2
            if A[i] % 2 == 1:
                l.append(j+1)
                break
print(min(l))
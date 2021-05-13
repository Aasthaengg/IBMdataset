n = int(input())
P = [int(input())-1 for _ in range(n)]
A = [0]*n
for i, p in enumerate(P):
    A[p] = i

#print(A)

m = 0
temp = 0
for i in range(1, n):
    if A[i-1] < A[i]:
        temp += 1
    else:
        m = max(m, temp)
        temp = 0
else:
    m = max(temp, m)
print(n-m-1)

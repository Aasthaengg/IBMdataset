n = int(input())
A = list(map(int,input().split()))
B = []
for i in range(n):
    B.append(A[i]-(i+1))
B.sort()
M = B[n//2]
res = 0
for b in B:
    res += abs(b-M)
print(res)
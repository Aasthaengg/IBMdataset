n, k = map(int, input().split())
A = [0]*n

for i in range(k):
    input()
    for j in list(map(int, input().split())):
        A[j-1] = 1
print(A.count(0))
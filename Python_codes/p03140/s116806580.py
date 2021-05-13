N = int(input())
A = input()
B = input()
C = input()
count = 0
for x in range(N):
    count += len(set([A[x], B[x], C[x]])) - 1
print(count)

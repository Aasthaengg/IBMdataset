N = int(input())
A = [0 for i in range(N)]
B = [0 for i in range(N)]

for i in range(N):
        A[i], B[i] = map(int, input().split())
        
max_a = max(A)
max_a_b = 0
for i in range(N):
    if A[i] == max_a:
        max_a_b = B[i]
        
print(max_a + max_a_b)
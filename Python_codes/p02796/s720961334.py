n = int(input())
A = []
for i in range(n):
    x, l = map(int, input().split())
    a = x - l
    b = x + l
    A.append((a, b))
A = sorted(A, key = lambda x:x[1])
cnt = 0
right = -float('inf')
for i in range(n):
    if right <= A[i][0] :
        cnt += 1
        right = A[i][1]
print(cnt)







N = int(input())
A = [int(a) for a in input().split()]

A.sort()
even = 0
odd = 0
num = A[0]
cnt = 0
for i in range(N+1):
    if i < N and num == A[i]:
        cnt += 1
    else:
        if cnt%2 == 0:
            even += 1
        else:
            odd += 1
        cnt = 1
        num = A[min(i, N-1)]

if even%2 == 0:
    ans = even + odd
else:
    ans = max(even + odd - 1, 1)
    
print(ans)
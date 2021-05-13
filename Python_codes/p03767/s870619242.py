N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
i = 1
n = 1
cnt = 0
while 2*i <= 2*N:
    cnt += A[n]
    i += 1
    n += 2
    
print(cnt)
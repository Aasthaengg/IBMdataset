import bisect
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort()
B.sort()
C.sort()

ans = 0
i = 0
j = 0
for b in B:
    while i < N and A[i] < b:
        i += 1
    while j < N and C[j] <= b:
        j += 1
    ans += i * (N-j)

print(ans)
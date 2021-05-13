n = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
ans = A[0]
cnt = 1
while cnt < n-1:
    ans += A[(cnt+1)//2]
    cnt += 1
print(ans)
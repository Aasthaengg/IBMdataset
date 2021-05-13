n = int(input())
A = list(map(int, input().split()))

m = sum(A)/n
ans = 0
cnt = m
for i in range(n):
    if abs(A[i]-m) < cnt:
        ans = i
        cnt = abs(A[i]-m)
print(ans)

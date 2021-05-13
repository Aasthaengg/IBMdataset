N,*A = map(int, open(0).read().split())
A.sort()
ans = 1
cs = 0
for i in range(N-1):
    cs += A[i]
    if cs * 2 >= A[i+1]:
        ans += 1
    else:
        ans = 1
print(ans)
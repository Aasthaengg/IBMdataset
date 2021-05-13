N = int(input())
A = [int(input()) for i in range(N)]

if A[0]:
    print(-1)
    exit()

ans = 0
for a,b in zip(A,A[1:]):
    if a+1 < b:
        print(-1)
        exit()
    if a+1 == b:
        ans += 1
    else:
        ans += b
print(ans)
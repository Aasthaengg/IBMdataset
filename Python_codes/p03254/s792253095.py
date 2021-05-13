N,x = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

if x < min(A):
    print(0)
    exit()

A.sort()
ans = 0
i = 0
while x > 0 and ans < N:
    if x >= A[i]:
        x -= A[i]
        ans += 1
        i += 1
    else:
        x = 0
        break

if x > 0:
    ans -= 1

print(ans)

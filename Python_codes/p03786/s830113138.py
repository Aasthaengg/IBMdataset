n = int(input())
A = list(map(int, input().split()))
A.sort()
sA = [0]
for i in range(n):
    sA.append(sA[i]+A[i])

A = A[::-1]
sA = sA[::-1]
ans = 1
for i in range(1,n):
    if 2*sA[i]>=A[i-1]:
        ans += 1
    else:
        break
print(ans)
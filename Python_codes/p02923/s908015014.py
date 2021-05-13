N = int(input())
A = list(map(int,input().split()))
right = [0]
A = A[::-1]
for i in range(1, N):
    if A[i] >= A[i - 1]:  right.append(right[-1] + 1)
    else:  right.append(0)
ans = max(right)
print(ans)
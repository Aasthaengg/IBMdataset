N = int(input())
A = [int(a) for a in input().split()]

ans = []
if abs(max(A)) > abs(min(A)):
    num = max(A)
    idx = A.index(num)
    for i in range(1, N):
        while A[i-1] > A[i]:
            A[i] += num
            ans.append([str(idx+1), str(i+1)])
            if A[i] > num:
                num = A[i]
                idx = i
else:
    num = min(A)
    idx = A.index(num)
    for i in range(N-2, -1, -1):
        while A[i] > A[i+1]:
            A[i] += num
            ans.append([str(idx+1), str(i+1)])
            if A[i] < num:
                num = A[i]
                idx = i
                
m = len(ans)
print(m)
for i in range(m):
    print(" ".join(ans[i]))
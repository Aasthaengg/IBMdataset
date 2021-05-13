n = int(input())
A = list(map(int,input().split()))

ans = []
maxim = A[0]
for i in range(1,n):
    if A[i] < maxim:
        ans.append(maxim-A[i])
    else:
        ans.append(0)
        maxim = A[i]
print(sum(ans))
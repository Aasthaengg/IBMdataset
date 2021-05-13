n = int(input())
A = list(map(int,input().split()))
ave = sum(A)/n
ans, idx = float('inf'), -1
for i in range(n):
    if abs(A[i]-ave) < ans:
        ans = abs(A[i]-ave)
        idx = i
print(idx)
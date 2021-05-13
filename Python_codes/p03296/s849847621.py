N = int(input())
A = list(map(int,input().split()))
row = 1
aim = A[0]
ans = 0
for i in range(1, N):
    if A[i] == aim:
        row += 1
    else:
        ans += row//2
        row = 1
        aim = A[i]
print(str(ans + row//2))
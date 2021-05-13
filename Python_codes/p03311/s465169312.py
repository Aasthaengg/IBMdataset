N = int(input())
A = list(map(int,input().split()))
B = []
for i in range(N):
    B.append(A[i] - i - 1)
B.sort()
cen = B[N//2]
sum = 0
for i in range(N):
    sum += abs(B[i]-cen)
print(sum)
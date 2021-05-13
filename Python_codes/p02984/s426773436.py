N = int(input())
A = list(map(int, input().split()))
S= sum(A)

R1 = S
for i in range(N//2):
    R1-=2*A[2*i+1]
R = [R1]

for j in range(1, N):
    R.append(A[j-1]*2-R[-1])

print(" ".join(str(n) for n in R))
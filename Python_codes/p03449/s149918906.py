N = int(input())
A = [list(map(int, input().split())) for _ in range(2)]
b = [0] + A[0]
c = [0] + A[1]

if N == 1:
    print(A[0][0] + A[1][0])
    exit()

for i in range(1, N):
    b[i+1] += b[i]
    c[i+1] += c[i]


ans = 0
for i in range(1, N):
    tmp = (b[i]-b[0]) + (c[-1]-c[i-1])
    ans = max(ans, tmp)

print(ans)
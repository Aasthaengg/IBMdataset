N = int(input())
A = map(int,input().split())

B = []
for i,a in enumerate(A):
    B.append(a-(i+1))
B.sort()
C = B[N//2-1:N//2+2]

MIN = 10**18
for j in C:
    ans = 0
    for i in B:
        ans += abs(i-j)

    MIN = min(ans,MIN)

print(MIN)
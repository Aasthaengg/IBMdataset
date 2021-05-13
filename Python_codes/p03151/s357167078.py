import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0
C = []
D = []
for i in range(n):
    if B[i] > A[i]:
        C.append(B[i] - A[i])
        ans += 1
    elif A[i] > B[i]:
        D.append(A[i] - B[i])

s = sum(C)
# print(s, C, D)

D.sort(reverse=True)
i = 0
while i < len(D) and s > 0:
    s -= D[i]
    ans += 1
    i += 1
# print(s)
if s > 0:
    ans = -1
print(ans)
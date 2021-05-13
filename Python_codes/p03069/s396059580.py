N = int(input())
S = input()
A = [0]

for s in S:
    if s == '.':
        A.append(A[-1] + 1)
    else:
        A.append(A[-1])
ans = float('inf')
for i in range(N + 1):
    ansi = (i - A[i]) + (A[-1] - A[i])
    ans = min(ans, ansi)
print(ans)

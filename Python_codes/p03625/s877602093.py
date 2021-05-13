N = int(input())
A = list(map(int, input().split()))
A = sorted(A, reverse=True)
kouho = set()

for i in range(N):
    if i == 0:
        continue
    elif A[i-1] == A[i]:
        kouho.add(A[i])
        if A.count(A[i]) >= 4 or len(kouho) >= 2:
            break
else:
    ans = 0

kouho = list(kouho)

if len(kouho) >= 2:
    ans = kouho[0] * kouho[1]
elif len(kouho) == 1:
    ans = kouho[0] ** 2

print(ans)
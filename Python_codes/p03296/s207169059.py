n = int(input())
A = list(map(int, input().split()))

ans = 0
B = [A[0]]
for i in range(1, n):
    if A[i] == B[-1]:
        B.append(0)
        ans += 1
    else:
        B.append(A[i])

print(ans)

N = int(input())
A = list(map(int, input().split()))
A.sort()

ru = [A[0]]
for i in range(1, N):
    ru.append(A[i]+ru[-1])

x = 0
for i in range(N-1, 0, -1):
    if ru[i-1]*2 < A[i]:
        x = i
        break

print(N-x)
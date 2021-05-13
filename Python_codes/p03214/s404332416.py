
N = int(input())
A = list(map(int, input().split()))

mean = sum(A)/N
mini = sum(A)
ans = 0

for i in range(len(A)):
    if abs(mean-A[i]) < mini:
        ans = i
        mini = abs(mean-A[i])

print(ans)

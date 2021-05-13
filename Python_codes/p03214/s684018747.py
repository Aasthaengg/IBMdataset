N = int(input())
A = list(map(int, input().split()))
avg = sum(A)/N
ansd = 1000000
for i in range(N):
    if abs(avg-A[i]) < ansd:
        ans = i
        ansd = abs(avg-A[i])
print(ans)
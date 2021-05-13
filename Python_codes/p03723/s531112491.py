A = list(map(int, input().split()))
ans = 0

while sum([A[i] % 2 for i in range(3)]) == 0:
    if A.count(A[0]) == 3:
        ans = -1
        break
    A = [(sum(A)-A[i])/2 for i in range(3)]
    ans += 1

print(ans)
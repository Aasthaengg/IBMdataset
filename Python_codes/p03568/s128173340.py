N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(3 ** N):
    mul = 1
    for j in range(N):
        mod = i // (3 ** j) % 3
        if mod == 0:
            mul *= A[j] - 1
        elif mod == 1:
            mul *= A[j]
        else:
            mul *= A[j] + 1
    if mul % 2 == 0:
        ans += 1
print(ans)

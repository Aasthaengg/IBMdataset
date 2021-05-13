N = int(input())
B = [int(x) for x in input().split()]
ans = B[0]
for i in range(N - 2):
    if B[i] <= B[i + 1]:
        ans += B[i]
    else:
        ans += B[i + 1]
ans += B[-1]
print(ans)

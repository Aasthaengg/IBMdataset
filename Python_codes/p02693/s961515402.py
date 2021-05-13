K = int(input())
A, B = [int(v) for v in input().split()]

ans = "NG"
for i in range(A, B + 1):
    if i % K == 0:
        ans = "OK"
        break

print(ans)
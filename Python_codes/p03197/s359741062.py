N = int(input())
A = [int(input()) for _ in range(N)]

ans = "second"
for a in A:
    if a%2 == 1:
        ans = "first"
        break
print(ans)
N = int(input())
A = list(map(int, input().split()))

ans = 1
for val in A:
    if val % 2 == 0:
        ans *= 2
print(3 ** N - ans)
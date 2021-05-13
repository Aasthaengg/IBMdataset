N = int(input())
A = [int(x) for x in input().split()]

last = 0
ans = 1

for i in range(N - 1):
    diff = A[i] - A[i + 1]
    if last == 0:
        if diff > 0:
            last = 1
        elif diff < 0:
            last = -1
    elif last * diff < 0:
        ans += 1
        last = 0

print(ans)
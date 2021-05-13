N = int(input())
D, X = list(map(int, input().split()))

count = 0
for i in range(1, N+1):
    A = int(input())
    for j in range(1, D+1):
        if (j - 1) * A + 1 <= D:
            count += 1
        else:
            break

result = count + X

print(result)
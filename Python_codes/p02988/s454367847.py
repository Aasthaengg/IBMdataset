def actual(n, P):
    count = 0

    for i in range(1, n - 1):
        a, b, c = P[i - 1], P[i], P[i + 1]

        if (a < b < c) or (a > b > c):
            count += 1

    return count

n = int(input())
P = list(map(int, input().split()))

print(actual(n, P))
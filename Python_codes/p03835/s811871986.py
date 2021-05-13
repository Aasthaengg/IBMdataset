def actual(K, S):
    count = 0

    for x in range(K + 1):
        for y in range(K + 1):
            z = S - (x + y)

            if 0 <= z <= K:
                count += 1

    return count

K, S = map(int, input().split())
print(actual(K, S))
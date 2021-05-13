def actual(K, S):
    count = 0

    for x in range(K + 1):
        for y in range(K + 1):
            z = S - (x + y)

            cond1 = (0 <= x <= K) and (0 <= y <= K) and (0 <= z <= K)
            cond2 = (x + y + z) == S

            if cond1 and cond2:
                count += 1

    return count

K, S = map(int, input().split())
print(actual(K, S))
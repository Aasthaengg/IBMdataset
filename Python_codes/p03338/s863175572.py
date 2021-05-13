def actual(N, S):
    count = 0

    for i in range(1, N):
        left_chars = set(S[:i])
        right_chars = set(S[i:])

        and_chars = left_chars & right_chars
        unique_chars = len(and_chars)

        if unique_chars > count:
            count = unique_chars

    return count

N = int(input())
S = input()

print(actual(N, S))
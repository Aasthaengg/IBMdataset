def actual(N, D, X, A):
    count = 0

    for a_i in A:
        for i in range(100+1):
            eating_day = 1 + (a_i * i)

            if eating_day <= D:
                count += 1

    return X + count

N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]

print(actual(N, D, X, A))

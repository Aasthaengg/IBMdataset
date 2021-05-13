N, X = map(int, input().split())

ARR = list(map(int, input().split()))


def calculate(n, x, arr):
    result = 0
    for i in range(1, n):
        sSum = arr[i - 1] + arr[i]
        if sSum <= x:
            continue

        diff = sSum - x

        if diff <= arr[i]:
            arr[i] -= diff
            result += diff
        else:
            result += diff
            arr[i] = 0

    print(result)


calculate(N, X, ARR)
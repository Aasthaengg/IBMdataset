def prod(arr):
    s = 0
    for x in arr:
        s += x
    return s


def main():
    N, K = (int(x) for x in input().split(" "))
    A = [int(x) for x in input().split(" ")]
    lastest_score = prod(A[0:K])
    result = ["No"] * (N-K+1)
    for i in range(1, N-K+1):
        current_score = lastest_score - A[i-1] + A[i + K-1]
        if lastest_score < current_score:
            result[i] = "Yes"
        lastest_score = current_score
    [print(x) for x in result[1:]]


if __name__ == '__main__':
    main()
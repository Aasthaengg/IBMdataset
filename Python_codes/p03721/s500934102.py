if __name__ == "__main__":
    N, K = [int(x) for x in input().split(" ")]
    arr = []
    for _ in range(N):
        a, b = [int(x) for x in input().split(" ")]
        arr.append((a, b))
    arr.sort()

    k = 0
    for a, b in arr:
        if k + b < K:
            k = k + b
        else:
            print(a)
            break


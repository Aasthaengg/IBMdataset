def track_number_needed(p, n_track):
    global W
    n_luggage = 0
    for j in range(n_track):
        weight_sum = 0
        while (weight_sum + W[n_luggage] <= p):
            weight_sum += W[n_luggage]
            n_luggage += 1
            if n_luggage == len(W):
                return n
    return n_luggage


def binary_search():
    global n
    global k
    left = 0
    right = 100000 * 10000
    while(right - left > 1):
        mid = (left + right) // 2
        n_luggage = track_number_needed(mid, k)
        if n_luggage >= n:
            right = mid
        else:
            left = mid
    return right
            


if __name__ == "__main__":
    n, k = map(int, input().split())
    W = [int(input()) for i in range(n)]
    print(binary_search())



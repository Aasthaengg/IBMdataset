if __name__ == "__main__":
    K, S = [int(x) for x in input().split(" ")]

    count = 0
    for x in range(0, K + 1):
        for y in range(0, K + 1):
            if 0 <= (S - x - y) <= K:
                count += 1
    print(count)

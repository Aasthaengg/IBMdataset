from collections import defaultdict


def main():
    n, w = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(n)]
    DP = defaultdict(int)
    DP[0] = 0
    for weight, value in items:
        exists = list(DP.items())
        for key, total in exists:
            new_key = key + weight
            new_total = total + value
            if DP[new_key] < new_total:
                DP[new_key] = new_total

    candidates = [0]
    for weight, value in sorted(DP.items()):
        if weight > w:
            break
        candidates.append(value)

    print(max(candidates))


if __name__ == "__main__":
    main()

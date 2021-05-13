from collections import defaultdict


def main():
    N = int(input())
    a = list(map(int, input().split()))

    color = defaultdict(int)

    for aa in a:
        if aa < 3200:
            color[aa//400] += 1
        else:
            color[8] += 1

    min_ans = len(color)
    max_ans = len(color)

    if 8 in color:
        min_ans = max(1, min_ans-1)
        max_ans += color[8] - 1

    print(min_ans, max_ans)


if __name__ == "__main__":
    main()

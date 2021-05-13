from bisect import bisect_left


def main():
    length = int(input())
    now_rate = list(map(int, input().split()))
    target_rate = list(map(int, input().split()))
    difference = [0] * length
    for i in range(length):
        difference[i] = now_rate[i] - target_rate[i]
    difference.sort()
    zero_index = bisect_left(difference, 0)
    answer = zero_index
    if zero_index > 0:
        has_prepared = difference[zero_index:]
        not_yet = sum(difference[:zero_index])
        for i in range(-1, -len(has_prepared) - 1, -1):
            not_yet += has_prepared[i]
            if not_yet >= 0:
                answer += abs(i)
                break
        else:
            answer = -1
    print(answer)


if __name__ == '__main__':
    main()


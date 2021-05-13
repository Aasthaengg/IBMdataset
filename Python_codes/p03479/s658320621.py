def solve():
    min_number, max_number = list(map(int, input().split()))

    current_number = min_number
    answer = 1

    while True:
        next_number = current_number * 2
        if next_number <= max_number:
            current_number = next_number
            answer += 1
        else:
            break

    print(answer)


solve()
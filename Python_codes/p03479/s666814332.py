def solve():
    min_number, max_number = list(map(int, input().split()))

    current_number = min_number
    answer = 0

    while current_number <= max_number:
        answer += 1
        current_number = current_number * 2

    print(answer)
    
solve()
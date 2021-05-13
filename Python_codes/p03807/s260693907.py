if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    odd_count = 0
    for aa in a:
        if aa % 2 == 1:
            odd_count += 1

    if odd_count % 2 == 1:
        print('NO')
    else:
        print('YES')

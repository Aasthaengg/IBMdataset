while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        for i, _ in enumerate(range(a)):
            if i % 2 == 0:
                if b % 2 == 1:
                    print('#.' * (b // 2) + '#')
                else:
                    print('#.' * (b // 2))
            else:
                if b % 2 == 1:
                    print('.#' * (b // 2) + '.')
                else:
                    print('.#' * (b // 2))
        print()

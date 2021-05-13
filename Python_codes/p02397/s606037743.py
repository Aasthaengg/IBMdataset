while True:
    results = list(map(str, sorted(map(int, input().split()))))
    if len(results) == len(list(filter(lambda item: item == '0', results))):
        break
    print(' '.join(results))
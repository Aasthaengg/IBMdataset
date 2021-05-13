while 1:
    line = list(map(int, input().split()))
    if not any(line):
        break
    print(*sorted(line))
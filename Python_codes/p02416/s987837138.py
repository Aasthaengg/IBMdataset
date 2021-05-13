while True:
    ans = 0
    x = raw_input()
    if x == "0":
        break
    print sum(map(int, x))
while True:
    input = raw_input()
    if input == '0': break
    num = map(int, input)
    print sum(num)

while True:
    value = [int(x) for x in raw_input()]
    if value[0] == 0:
        break
    print(sum(value))
while True:
    tmp = raw_input()
    if tmp == "-":
        break
    m = input()
    for i in range(m):
        h = input()
        tmp = tmp[h:] + tmp[:h]

    print tmp
while True:
    integer = input()
    if int(integer) == 0:
        break
    print(sum(list(map(int, list(integer)))))
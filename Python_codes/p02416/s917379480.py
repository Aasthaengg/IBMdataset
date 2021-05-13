while True:
    num = input()
    if num == "0":
        break
    print(sum(map(int, list(num))))
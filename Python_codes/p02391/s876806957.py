def main(arg):
    arg = str(arg)
    numbers = [int(x)for x in arg.split(" ")]
    a,b = numbers[0],numbers[1]
    if a > b:
        return "a > b"
    elif a < b:
        return "a < b"
    elif a == b:
        return "a == b"
    return False


if __name__ == '__main__':
    print(main(input()))
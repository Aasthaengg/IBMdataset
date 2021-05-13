def main(arg):
    arg = str(arg)
    numbers = [int(x)for x in arg.split(" ")]
    a,b,c = numbers[0],numbers[1],numbers[2]
    if a < b < c:
        return "Yes"
    return "No"


if __name__ == '__main__':
    print(main(input()))
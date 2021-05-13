import sys

def main():
    inputData = input().strip().split(" ")
    result = 0
    ball = int(inputData[0])
    people = int(inputData[1])

    if people <= 1:
        return 0

    if ball > people:
        result = ball - people
        result += 1

    else:
        return 0

    result -= 1

    return result


if __name__ == '__main__':
    print(main())
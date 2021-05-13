def maximum_profit():
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    maxpro = numbers[1] - numbers[0]
    minnum = numbers[0]
    for i in range(1, len(numbers)):
        if maxpro < (numbers[i] - minnum):
            maxpro = (numbers[i] - minnum)
        if numbers[i] < minnum:
            minnum = numbers[i]
    print(maxpro)


if __name__ == "__main__":
    maximum_profit()
if __name__ == '__main__':
    key_in = input()
    data = [int(x) for x in key_in.split(' ')]
    a = data[0]
    b = data[1]
    c = data[2]

    divisor = 0
    for i in range(a, b+1):
        if c % i == 0:
            divisor += 1
    print(divisor)
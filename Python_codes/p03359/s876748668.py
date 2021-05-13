def main(a, b):
    if b < a:
        return a-1
    else:
        return a


if __name__ == '__main__':
    a, b = map(int, input().split(' '))
    print(main(a, b))

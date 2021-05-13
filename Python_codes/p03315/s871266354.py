def main():
    s = input()

    ret = 0
    for c in s:
        ret = eval(str(ret) + c + '1')
    print(ret)


if __name__ == '__main__':
    main()

def main():
    count, rate = (int(i) for i in input().rstrip().split(' '))
    ans = rate if count >= 10 else rate + (100 * (10 - count))
    print(str(ans))


if __name__ == '__main__':
    main()

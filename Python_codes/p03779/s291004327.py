
def main():
    n = int(input())
    pos = 0
    count = 0
    while pos < n:
        count += 1
        pos += count
    print(count)


if __name__ == '__main__':
    main()
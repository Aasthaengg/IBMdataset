def main():
    s = list(input())
    count = 0
    for i in s:
        if i == 'o':
            count += 1
    print(700 + 100 * count)
if __name__ == '__main__':
    main()
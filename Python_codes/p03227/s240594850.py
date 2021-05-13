def main():
    s = str(input())
    if len(s) == 2:
        print(s)
    elif len(s) == 3:
        print(s[::-1])

if __name__ == '__main__':
    main()
def main():
    string = input()
    print(string if len(string) == 2 else string[::-1])


if __name__ == '__main__':
    main()


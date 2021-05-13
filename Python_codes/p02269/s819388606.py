def main():
    dictionary = set()
    for _ in range(int(input())):
        command = input().split()
        if command[0] == 'insert':
            dictionary.add(command[1])
        else:
            print('yes' if command[1] in dictionary else 'no')


if __name__ == '__main__':
    main()


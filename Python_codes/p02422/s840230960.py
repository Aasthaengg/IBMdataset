def main():
    string = input()
    q = int(input())
    for _ in range(q):
        command = input().split()
        a = int(command[1])
        b = int(command[2])
        if command[0] == 'print':
            print(string[a:b+1])
        elif command[0] == 'reverse':
            if a == b:
                reversed_string = string[a]
            else:
                c = a-1 if a is not 0 else None
                reversed_string = string[b:c:-1]
            string = string[:a] + reversed_string + string[b+1:]
        elif command[0] == 'replace':
            string = string[:a] + command[3] + string[b+1:]


if __name__ == '__main__':
    main()


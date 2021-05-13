# ABC069 B

def main():
    s = input()

    print(s[0] + str(len(s[1:-1])) + s[-1])

if __name__ == '__main__':
    main()
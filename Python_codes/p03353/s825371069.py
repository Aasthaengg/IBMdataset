def main():
    string = input()
    range_ = int(input())
    substrings = []
    for i in range(len(string)):
        for j in range(1, range_ + 1):
            substrings.append(string[i:i + j])
    substrings = list(set(substrings))
    substrings.sort()
    print(substrings[range_ - 1])


if __name__ == '__main__':
    main()

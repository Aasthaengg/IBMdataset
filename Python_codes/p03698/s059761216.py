def main():
    s = input()
    answer = 'yes'

    for i in range(len(s)-1):
        if s[i] in s[i+1:]:
            answer = 'no'
    print(answer)


if __name__ == "__main__":
    main()

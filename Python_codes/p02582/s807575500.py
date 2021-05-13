def main():
    S = input()
    count = 1
    if 'R' in S:
        for i in range(len(S)-1):
            if S[i] == S[i+1] == 'R':
                count += 1
        print(count)

    else:
        print(0)


if __name__ == '__main__':
    main()
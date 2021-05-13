def main():
    S = input()
    w = int(input())

    answer = ""

    for i in range(0, len(S), w):
        answer += S[i]

    print(answer)

if __name__ == '__main__':
    main()

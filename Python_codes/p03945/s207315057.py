def main():
    S = input()
    answer = 0

    for i in range(1,len(S)):
        if S[i-1] != S[i]:
            answer += 1

    print(answer)

if __name__ == '__main__':
    main()

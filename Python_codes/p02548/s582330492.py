def main():
    N = int(input())

    answer = 0
    for A in range(1, N):
        answer = answer + (N - 1) // A

    print(answer)

if __name__ == "__main__":
    main()
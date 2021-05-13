def main():
    n = int(input())
    k = int(input())
    score = 1
    for _ in range(n):
        if score < k:
            score *= 2
        else:
            score += k
    print(score)


if __name__ == "__main__":
    main()

def main():
    n, k, q = map(int, input().split())
    score_list = [k - q for _ in range(n)]

    for _ in range(q):
        a = int(input())
        score_list[a - 1] += 1

    for score in score_list:
        if score > 0:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()

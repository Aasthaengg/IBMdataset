# code-festival-2016-qualbA - Signboard
def main():
    S = input().rstrip()
    C = "CODEFESTIVAL2016"
    ans = sum(i != j for i, j in zip(S, C))
    print(ans)


if __name__ == "__main__":
    main()
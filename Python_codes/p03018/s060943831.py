def main():
    S = input()
    S = S.replace("BC", "D")

    ans = 0
    count_A = 0
    for c in S:
        if c == "A":
            count_A += 1
        elif c == "D":
            ans += count_A
        else:
            count_A = 0
    print(ans)

if __name__ == "__main__":
    main()
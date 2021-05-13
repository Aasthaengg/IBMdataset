# ARC062D - AtCoDeerくんと変なじゃんけん / AtCoDeer and Rock-Paper (ABC046D)
def main():
    # p as much as possible (len(S) // 2)
    S = input().rstrip()
    ans = len(S) // 2 - S.count("p")
    print(ans)


if __name__ == "__main__":
    main()
# code-festival-2016-qualc
def main():
    S = input()
    flg = 0 <= S.find("C") < S.rfind("F")
    print("Yes" if flg else "No")


if __name__ == "__main__":
    main()
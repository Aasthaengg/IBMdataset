# cf17-finalA - AKIBA
def main():
    S = input().rstrip()
    SR = S.replace("A", "")
    flg = SR == "KIHBR" and "AA" not in S and "KIH" in S
    print("YES" if flg else "NO")


if __name__ == "__main__":
    main()
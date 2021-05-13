def resolve():
    abcd = list(input().split())
    print("YES" if "".join(sorted(abcd)) == "1479" else "NO")


if __name__ == "__main__":
    resolve()

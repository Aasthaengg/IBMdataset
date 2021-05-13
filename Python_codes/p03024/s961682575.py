def resolve():
    s = input()
    print("YES" if s.count("o") + 15 - len(s) >= 8 else "NO")


if __name__ == "__main__":
    resolve()

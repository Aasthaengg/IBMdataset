def main():
    s = input()
    x = 15 - len(s)

    if (s.count("o") + x) >= 8:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
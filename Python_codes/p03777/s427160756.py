def main():
    a, b = input().split()
    if a == "H" and b == "H":
        ans = 'H'
    elif a == 'D' and b == 'H':
        ans = 'D'
    elif a == "D" and b == "D":
        ans = "H"
    else:
        ans = "D"
    print(ans)


if __name__ == "__main__":
    main()

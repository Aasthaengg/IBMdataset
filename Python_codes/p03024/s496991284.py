def main():
    S = input()
    if S.count('o') >= 8 - (15 - len(S)):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()

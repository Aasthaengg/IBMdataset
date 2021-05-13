def main():
    S = list(input().rstrip())
    if len(S) == len(set(S)):
        print("yes")
    else:
        print("no")


if __name__ == '__main__':
    main()

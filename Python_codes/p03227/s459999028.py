def main():
    s = input().rstrip()
    if len(s) == 2:
        print(s)
    else:
        print(s[::-1])

if __name__ == "__main__":
    main()

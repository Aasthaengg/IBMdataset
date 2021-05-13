def main():
    n = int(input())
    s_set = set(input().split())
    if "Y" in s_set:
        print("Four")
    else:
        print("Three")


if __name__ == "__main__":
    main()

def main():
    people_num = int(input())
    hats = input()
    print("Yes" if hats.count("B") < hats.count("R") else "No")


if __name__ == '__main__':
    main()


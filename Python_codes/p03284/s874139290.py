def main():
    rice_cookie, participants = map(int, input().split(" "))
    if not rice_cookie % participants:
        print(0)
    else:
        print(1)


if __name__ == '__main__':
    main()
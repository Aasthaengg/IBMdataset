def main():
    balls, people = map(int, input().split())
    print(0 if people == balls or people == 1 else balls - people)


if __name__ == '__main__':
    main()


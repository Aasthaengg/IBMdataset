def main():
    print("Yes" if len(set(list(map(int, input().split())))) == 1 else "No")


if __name__ == '__main__':
    main()


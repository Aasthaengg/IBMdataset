
def main():
    n = input().split()
    if n[1] == '+':
        print(int(n[0]) + int(n[2]))
    else:
        print(int(n[0]) - int(n[2]))


if __name__ == "__main__":
    main()

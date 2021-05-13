def call(a):
    if a % 3 == 0:
        return True

    while a != 0:
        if a % 10 == 3:
            return True

        a //= 10

    return False

def main():
    n = int(input())

    for i in range(1, n + 1):
        if call(i):
            print(" {0}".format(i), end="")

    print("")

if __name__ == "__main__":
    main()
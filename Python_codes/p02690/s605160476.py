def main():
    x = int(input())
    for i in range(-120, 121):
        for j in range(-120, 121):
            if i**5 - j**5 == x:
                print(i, j)
                return

if __name__ == "__main__":
    main()
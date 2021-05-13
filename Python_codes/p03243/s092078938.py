def main():
    s=int(input())
    for n in range(111, 1000, 111):
        if s <= n:
            print(n)
            return

if __name__ == "__main__":
    main()
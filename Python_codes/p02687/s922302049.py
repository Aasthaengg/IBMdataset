def main():
    s = input()
    print(list(set(["ABC", "ARC"])-set([s]))[0])

if __name__ == "__main__":
    main()
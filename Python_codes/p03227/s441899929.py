def main():
    x = list(input())
    if len(x) > 2:
        x.reverse()
    print("".join(x))

if __name__ == "__main__":
    main()

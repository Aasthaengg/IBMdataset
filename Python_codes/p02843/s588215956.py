def main():
    X = int(input())
    for i in range(1000):
        if 100*i <= X <= 105*i:
            print(1)
            return
    print(0)

if __name__ == "__main__":
    main()

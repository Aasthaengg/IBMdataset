def main():
    x, y = map(int, input().split())
    y_devided = y // x
    y_devided_binary = format(y_devided, "b")
    print(len(y_devided_binary))

if __name__ == "__main__":
    main()
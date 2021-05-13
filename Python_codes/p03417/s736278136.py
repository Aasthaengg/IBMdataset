def main():
    width, height = map(int, input().split(" "))
    if width * height == 1:
        print(1)
    elif width == 1:
        print(height - 2)
    elif height == 1:
        print(width - 2)
    else:
        print((height - 2) * (width - 2))


if __name__ == '__main__':
    main()
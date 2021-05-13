def main():
    width, height, target = map(int, input().split())
    answer = False
    if target == 0:
        answer = True
    else:
        for i in range(height):
            if answer:
                break
            for j in range(width):
                if (width - j) * (height - i) + i * j == target:
                    answer = True
                    break
    print("Yes" if answer else "No")


if __name__ == '__main__':
    main()


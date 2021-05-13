def main():
    plates, height, width = map(int, input().split())
    answer = 0
    for _ in range(plates):
        h, w = map(int, input().split())
        if height <= h and width <= w:
            answer += 1
    print(answer)


if __name__ == '__main__':
    main()


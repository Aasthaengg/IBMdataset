def main():
    height, width = map(int, input().split())
    color = int(input())
    limits = list(map(int, input().split()))
    answer = []
    for i in range(color):
        answer = answer + [i + 1] * limits[i]
    for i in range(height):
        if i % 2:
            print(" ".join(map(str, list(reversed(answer[i * width:(i + 1) * width:])))))
        else:
            print(" ".join(map(str, answer[i * width:(i + 1) * width])))


if __name__ == '__main__':
    main()


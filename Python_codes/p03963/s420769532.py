def main():
    ball_num, color_num = map(int, input().split())
    print(color_num * pow(color_num - 1, ball_num - 1))


if __name__ == '__main__':
    main()


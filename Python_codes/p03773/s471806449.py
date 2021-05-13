def main():
    now_time, start_in = map(int, input().split())
    print((now_time + start_in) % 24)


if __name__ == '__main__':
    main()


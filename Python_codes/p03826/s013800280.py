def main():
    lengths = list(map(int, input().split()))
    area = [lengths[0] * lengths[1], lengths[2] * lengths[3]]
    print(area[0] if area[0] > area[1] else area[1])


if __name__ == '__main__':
    main()


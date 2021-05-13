def main():
    population, a_reader, b_reader = map(int, input().split())
    print(min(a_reader, b_reader), max(a_reader + b_reader - population, 0))


if __name__ == '__main__':
    main()


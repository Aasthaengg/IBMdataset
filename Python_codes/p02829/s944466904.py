def main():
    cands = {1, 2, 3}
    for _ in range(2):
        cands.discard(int(input()))
    print(cands.pop())


if __name__ == '__main__':
    main()

class AtCoder:
    def main(self):
        a, b, h = [int(input()) for _ in range(3)]
        return (a + b) * h // 2


if __name__ == '__main__':
    print(AtCoder().main())
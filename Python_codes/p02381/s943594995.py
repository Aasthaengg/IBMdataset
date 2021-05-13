from statistics import pstdev


def main():
    while int(input()) != 0:
        scores = map(float, input().split())
        print('{:.5f}'.format(pstdev(scores)))


if __name__ == '__main__':
    main()


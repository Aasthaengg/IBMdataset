def main():
    n, k = [int(x) for x in input().split()]
    scores = [int(x) for x in input().split()]

    for index, new in enumerate(scores[k:]):
        if scores[index] < new:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()

def main():
    ATCG = 'ATCG'

    b = input()
    i = ATCG.index(b)
    print(ATCG[i ^ 1])


if __name__ == '__main__':
    main()

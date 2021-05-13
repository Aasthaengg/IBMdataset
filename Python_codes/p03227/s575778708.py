# tenka1-2018-beginnerA - Measure
def main():
    S = input().rstrip()
    flg = len(S) == 2
    print(S if flg else S[::-1])


if __name__ == "__main__":
    main()
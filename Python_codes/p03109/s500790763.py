import datetime


def main():
    s = datetime.datetime.strptime(input(), "%Y/%m/%d")
    if s <= datetime.datetime(2019, 4, 30):
        print("Heisei")
    else:
        print("TBD")


if __name__ == '__main__':
    main()

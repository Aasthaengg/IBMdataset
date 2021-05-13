import datetime as d
def main():
    s = d.datetime.strptime(input(), "%Y/%m/%d")
    s = d.date(s.year, s.month, s.day)
    if s <= d.date(2019,4,30):
        print("Heisei")
    else:
        print("TBD")

if __name__ == "__main__":
    main()
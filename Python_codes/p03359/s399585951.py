import datetime
def main():
    a, b = map(int, input().split())
    cnt = 0
    for i in range(1, 13):
        if datetime.date(2018, i, i) <= datetime.date(2018, a, b):
            cnt += 1
    print(cnt)
if __name__ == "__main__":
    main()
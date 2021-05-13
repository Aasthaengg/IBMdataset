# A - Odds of Oddness
def main():
    cnt = 0
    n = int(input())
    for i in range(1,n+1):
        if i % 2 != 0:
            cnt += 1
    print(cnt/n)

if __name__ ==  "__main__":
    main()
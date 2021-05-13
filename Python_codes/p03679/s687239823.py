def main():
    x,a,b = map(int,input().split())
    now = b - a
    if now <= 0:
        print("delicious")
    elif now <= x:
        print("safe")
    else:
        print("dangerous")

if __name__ == '__main__':
    main()

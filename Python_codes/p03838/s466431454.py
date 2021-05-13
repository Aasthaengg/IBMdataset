def main():
    x, y = map(int, input().split())
    print(min(abs(x+y), abs(~x+y))+1)
if __name__ == '__main__':
    main()
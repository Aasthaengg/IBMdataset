
def main():
    a,b,x = map(int,input().split())
    answer = "YES" if a <= x <= (a+b) else "NO"
    print(answer)


if __name__ == '__main__':
    main()

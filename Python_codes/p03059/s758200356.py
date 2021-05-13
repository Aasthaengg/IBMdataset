def main():
    a, b, t = map(int, input().split())
    time = t/a
    ans = int(time) * b
    print(int(ans))
if __name__ == '__main__':
    main()
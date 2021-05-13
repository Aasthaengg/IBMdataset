def main():
    x, y = map(int, input().split())
    last_num = x
    ans = 1
    while 1:
        if last_num * 2 <= y:
            last_num *= 2
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()
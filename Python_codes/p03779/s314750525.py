def main():
    x = int(input())
    sum = 0
    ans = 0
    while sum < x:
        sum += ans + 1
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()

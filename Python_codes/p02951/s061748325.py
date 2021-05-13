def main():
    t = list(map(int, input().split()))
    ans = t[1] + t[2] - t[0]
    print(ans) if ans >= 0 else print(0)

if __name__ == '__main__':
    main()

def main():
    H, a,b = list(map(int, input().split()))
    ans = max(a,b) - (min(a,b) + H)
    print(ans) if ans >= 0 else print(0)

if __name__ == '__main__':
    main()

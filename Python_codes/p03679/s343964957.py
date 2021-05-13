def main():
    x, a, b = map(int, input().split())
    if b <= a:
        ans = 'delicious'
    else:
        if b <= (x+a):
            ans = 'safe'
        else:
            ans = 'dangerous'
    print(ans)


if __name__ == "__main__":
    main()

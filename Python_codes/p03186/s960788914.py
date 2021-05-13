def main():
    a, b, c = map(int, input().split())
    ans = 0
    if c > 0:
        ans += 1
        c -= 1
    if c <= b:
        ans += c + b
    else:
        ans += 2*b
        c -= b
        ans += min(c, a)
    print(ans)

if __name__ == "__main__":
    main()
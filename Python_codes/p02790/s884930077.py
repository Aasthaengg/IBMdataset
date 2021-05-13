def main():
    a, b = map(int, input().split())
    l = [str(a) * b, str(b) * a]
    ans = sorted(l)[0]
    print(ans)

if __name__ == '__main__':
    main()
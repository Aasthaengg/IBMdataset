def main():
    a, b, c = map(int, input().split())
    total = b // a
    if total > c:
        print(c)
    else:
        print(total)

main()
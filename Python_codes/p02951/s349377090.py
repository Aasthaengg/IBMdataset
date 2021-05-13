def main():
    a, b, c = map(int, input().split())
    ans = 0 if b + c - a <= 0 else b + c -a
    print(ans)

main()

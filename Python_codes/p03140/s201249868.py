def main():
    n = int(input())
    a = input().rstrip()
    b = input().rstrip()
    c = input().rstrip()
    ans = 0
    for i in range(n):
        if a[i] == b[i] == c[i]:
            continue
        elif a[i] == b[i] or b[i] == c[i] or c[i] == a[i]:
            ans += 1
        else:
            ans += 2
    print(ans)

if __name__ == "__main__":
    main()
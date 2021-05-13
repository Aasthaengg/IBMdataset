def main():
    w, a, b = map(int, input().split())
    a1, a2 = a, a+w
    b1, b2 = b, b+w
    if a1 <= b1 and b1 <= a2:
        ans = 0
    elif a1 <= b2 and b2 <= a2:
        ans = 0
    else:
        if b2 <= a1:
            ans = a1 - b2
        elif a2 <= b1:
            ans = b1 - a2
    print(ans)


if __name__ == "__main__":
    main()

def main():
    A, B = (int(x) for x in input().split())
    if (A % 2 == 0 and B % 2 == 0) or (A % 2 == 1 and B % 2 == 1):
        ans = int((A + B) / 2)
    else:
        ans = "IMPOSSIBLE"
    print(ans)


if __name__ == "__main__":
    main()

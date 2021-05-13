def main():
    n, a, b = map(int, input().split())
    ans_max = min(a, b)
    if n >= a + b:
        ans_min = 0
    else:
        ans_min = (a + b) - n
    print(str(ans_max) + " " + str(ans_min))


if __name__ == "__main__":
    main()

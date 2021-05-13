def main():
    a, b, x = map(int, input().split())
    if a == 0:
        left = 0
    else:
        left = (a-1)//x + 1

    if b == 0:
        right = 1
    else:
        right = b//x + 1 

    print(right - left)
if __name__ == "__main__":
    main()
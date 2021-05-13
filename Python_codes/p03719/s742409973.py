def main():
    a, b, c = map(int, input().split())
    if a <= c and c <= b:
        ans = 'Yes'
    else:
        ans = 'No'
    print(ans)


if __name__ == "__main__":
    main()

def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for v in a:
        if v % 2 == 1:
            cnt += 1
    if cnt % 2 == 1:
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    main()
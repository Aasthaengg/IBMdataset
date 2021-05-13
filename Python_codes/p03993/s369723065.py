def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i, x in enumerate(a):
        if a[x-1] == i+1:
            cnt += 1

    print(cnt//2)

if __name__ == '__main__':
    main()

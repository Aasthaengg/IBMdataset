def main():
    n = int(input())
    a, b = map(int, input().split())
    p = list(map(int, input().split()))
    cnt = [0]*3
    for v in p:
        if v <= a:
            cnt[0] += 1
        elif v <= b:
            cnt[1] += 1
        else:
            cnt[2] += 1
    print(min(cnt))

if __name__ == "__main__":
    main()
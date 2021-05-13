def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt, nega, posi = 0, 0, []
    for x, y in zip(a, b):
        if x < y:
            nega += y - x
            cnt += 1
        else:
            posi.append(x - y)
    if sum(posi) - nega < 0:
        print(-1)
        exit()
    posi.sort(reverse=True)
    i = 0
    while nega > 0:
        nega -= posi[i]
        cnt += 1
        i += 1
    print(cnt)

if __name__ == "__main__":
    main()
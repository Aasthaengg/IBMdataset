def main():
    k, s = map(int, input().split())
    cnt = 0
    for x in range(k+1):
        for y in range(k+1):
            if s - x - y >= 0 and s - x - y <= k:
                    # print(x, y, s-x-y)
                    cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
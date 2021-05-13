def main():
    N, D = map(int, input().split())
    cnt = 0
    while True:
        a, b = divmod(N, (2*D+1))
        cnt += a
        if 2*D + 1 > b:
            if b > 0:
                cnt += 1
            break
    print(cnt)
main()
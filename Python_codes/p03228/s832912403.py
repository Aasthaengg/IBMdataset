#!/snap/bin/pypy3

def main():
    A, B, K = map(int, input().split())

    cookies = [A, B]
    for i in range(K):
        if cookies[i%2] % 2:
            cookies[i%2] -= 1

        cookies[(i+1)%2] += cookies[i%2] // 2
        cookies[i%2] //= 2

    print(*cookies)


if __name__ == '__main__':
    main()

def main():
    A, B, K = map(int, input().split())
    cookies = [A, B]
    for i in range(K):
        cookies[i & 1] //= 2
        cookies[(i+1) & 1] += cookies[i & 1]
    print(*cookies)


if __name__ == "__main__":
    main()

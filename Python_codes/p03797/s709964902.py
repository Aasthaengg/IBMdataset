def main():
    N, M = map(int, input().split())

    cnt = 0
    cnt = min(N, M//2)
    M -= 2*cnt
    if M > 0:
        cnt += M//4
    print(cnt)
        
if __name__ == "__main__":
    main()
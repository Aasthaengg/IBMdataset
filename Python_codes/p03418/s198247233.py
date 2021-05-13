def main():
    n, k = map(int, input().split())
    if k == 0:
        print(n ** 2)
        exit()
    cnt = 0
    for i in range(1, n+1):
        p, r = divmod(n, i)
        cnt += max(0, p * (i - k)) + max(0, r - k + 1)
    
    print(cnt)
if __name__=='__main__':
    main()
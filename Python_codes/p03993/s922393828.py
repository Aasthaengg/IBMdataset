def main():
    n = int(input())
    a = list(map(int,input().split()))
    cnt = 0
    for i in range(n):
        if (i+1) < a[i] and a[a[i]-1] == (i+1):
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()

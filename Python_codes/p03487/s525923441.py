def main():
    n = int(input())
    a = list(map(int,input().split()))
    from collections import Counter
    c = Counter(a)
    cnt = 0
    for i,j in c.items():
        if i == 1:
            cnt += max(j-1,0)
        else:
            cnt += j%i
    print(cnt)

if __name__ == '__main__':
    main()

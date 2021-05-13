def main():
    n = int(input())
    a = list(map(int, input().split()))
    a_s = sorted(a)
    cnt = 0
    for i in range(n):
        if a[i] != a_s[i]:
            cnt += 1
    if cnt == 2 or cnt == 0:
        print('YES')
    else:
        print('NO')
        
if __name__ == '__main__':
    main()
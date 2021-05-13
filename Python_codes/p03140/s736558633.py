def slove():
    import sys
    input = sys.stdin.readline
    n = int(input().rstrip('\n'))
    a = str(input().rstrip('\n'))
    b = str(input().rstrip('\n'))
    c = str(input().rstrip('\n'))
    cnt = 0
    for i in range(n):
        if a[i] == b[i] == c[i]:
            continue
        elif a[i] == b[i]:
            cnt += 1
        elif b[i] == c[i]:
            cnt += 1
        elif a[i] == c[i]:
            cnt += 1
        else:
            cnt += 2
    print(cnt)


if __name__ == '__main__':
    slove()

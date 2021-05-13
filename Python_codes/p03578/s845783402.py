import collections
def main():
    n = int(input())
    d = list(map(int,input().split()))
    m = int(input())
    t = list(map(int,input().split()))

    if n < m:
        print('NO')
        return

    cnt_d = collections.Counter(d)
    cnt_t = collections.Counter(t)

    for i, k in enumerate(cnt_t.keys()):
        if cnt_d[k] >= cnt_t[k]:
            continue
        else:
            print('NO')
            return
    print('YES')


if __name__ == '__main__':
    main()

def srch(i, l, Lng, Dst):
    if Lng[i] != -1 and Lng[i] < l:
        return
    Lng[i] = l
    if Dst[i] is not None and len(Dst[i]) > 0:
        for c in Dst[i]:
            srch(c,l+1, Lng, Dst)

def main():
    num = int(input())
    Dst = [None for i in range(num + 1)]
    Lng = [-1] * (num + 1)
    
    for n in range(1, num+1):
        a = list(map(int,input().split()))
        u = a[0]
        if a[1] > 0:
            Dst[u] = a[2:]

    srch(1, 0, Lng, Dst)

    for n in range(1, num+1):
        l = Lng[n]
        if l > num:
            l = -1
        print("{} {}".format(n,l))

if __name__ == '__main__':
    main()
def main():
    import math
    import sys
    input = sys.stdin.readline

    n,k = map(int,input().split())
    a = sorted(list(map(int,input().split())))
    f = sorted(list(map(int,input().split())),reverse=True)
    check = []
    for i in range(n):
        check.append((a[i]*f[i],a[i],f[i]))

    def search(x):
        count = 0

        for i,j,k in check:
            if i > x:
                y = math.floor(x/k)
                count += j-y
        return count

    left = -1
    right = 10**12+2
    while right > left+1:
        mid = (right+left)//2
        if search(mid) > k:
            left = mid
        else:
            right = mid
    print(right)
if __name__ == "__main__":
    main()
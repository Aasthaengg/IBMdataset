def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    def gcd(x,y):
        r = x%y
        if r==0:
            return y
        return gcd(y, r)

    n, k =map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    c = a[0]
    for i in range(n):
        c = gcd(a[i], c)
    if k%c == 0 and k <= a[0]:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')
    

    
if __name__ == '__main__':
    main()
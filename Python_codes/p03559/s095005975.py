
        
def main():
    import sys
    from bisect import bisect_left, bisect_right
    def input(): return sys.stdin.readline().rstrip()

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    b.sort()
    c.sort()
    ans = 0
    for j in range(n):
        i = bisect_left(a, b[j])
        k = bisect_right(c, b[j])
        ans += i*(n-k)

    print(ans)
        




                
if __name__ == '__main__':
    main()
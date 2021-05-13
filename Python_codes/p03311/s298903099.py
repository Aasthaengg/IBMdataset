
        
def main():
    import sys
    from bisect import bisect_left, bisect_right
    def input(): return sys.stdin.readline().rstrip()

    n = int(input())
    a = list(map(int, input().split()))
    a = [x-i-1 for i, x in enumerate(a)]
    a.sort()
    mid = a[n//2]
    ans = sum([abs(x-mid) for x in a])
    print(ans)




                
if __name__ == '__main__':
    main()
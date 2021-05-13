def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    mdl = a[0]//2
    if a[0]%2 == 0:
        dist = [abs(x-mdl) for x in a[1:]]
    else:
        dist = [abs(x-mdl) if x <= mdl else abs(x - mdl - 1) for x in a[1:]]
    idx = min(range(1,n), key=lambda i: dist[i-1])
    print(a[0], a[idx])
    
        
    
    
if __name__ == '__main__':
    main()
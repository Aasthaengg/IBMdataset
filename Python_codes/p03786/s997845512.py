def main():
    import sys

    def input(): return sys.stdin.readline().rstrip()

    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    s = [0]
    for i in range(n-1):
        s.append(s[-1]+a[~i])
    s.reverse()
    for i in range(n):
        if a[i] >  s[i]*2:
            break
    print(i+1)  

    
if __name__ == '__main__':
    main()
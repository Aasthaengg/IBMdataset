def main():
    n = int(input())
    a, b = [None]*n, [None]*n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    if n%2:
        print(b[n//2]-a[n//2]+1)
    else:
        bm = b[n//2]+b[n//2-1]
        am = a[n//2]+a[n//2-1]
        print(bm-am+1)
        

if __name__ == "__main__":
    main()
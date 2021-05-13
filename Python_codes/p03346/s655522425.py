import sys
# import io, os
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
def input():
    return sys.stdin.readline()[:-1]
def main():
    n = int(input())
    a = [int(input()) for k in range(n)]
    b = [[a[k],k] for k in range(n)]
    b = sorted(b)
    c = [b[k][1] for k in range(n)]
    c = [-1] + c + [100000]
    t = 0
    ans = 0
    for k in range(1,n+1):
        if c[k-1] < c[k]:
            t += 1
        else:
            t = 1
        ans = max(ans,t)
    print(n-ans)
if __name__ == '__main__':
    main()

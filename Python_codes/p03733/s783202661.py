import sys
def input():
    return sys.stdin.readline()[:-1]
def main():
    N, T = map(int,input().split())
    t = list(map(int,input().split()))
    prev = 0
    end = 0
    ans = 0
    for e in t:
        if end < e:
            ans += end-prev
            prev = e
            end = e + T
        else:
            end = e + T
    ans += end - prev
    print(ans)
if __name__ == '__main__':
    main()

from sys import setrecursionlimit, exit
setrecursionlimit(1000000000)

def main():
    n = int(input())
    a = list(map(int, input().split()))
    r = sum(a)
    l = 0
    ans = r
    for i in a:
        l += i
        r -= i
        ans = min(ans, abs(r - l))
        if l >= r:
            break
    print(ans)

main()
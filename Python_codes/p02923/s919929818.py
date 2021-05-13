def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n = int(input())
    h = list(reversed(Input()))
    val = 0
    ans = 0
    for i in range(1, n):
        if h[i-1] <= h[i]: val += 1
        else: val = 0
        ans = max(ans, val)
        
    print(ans)
main()
import sys

input = sys.stdin.readline

def main():
    ans = 0
    x, k, d = map(int, input().split())
    ans = abs(x) - (d * min(k, abs(x)//d))
    t = k - abs(x)//d
    if t%2 != 0 and t > 0:
        ans = min(abs(ans-d), abs(ans+d))
    print(ans)

main()


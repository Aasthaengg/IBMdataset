import sys
def input(): return sys.stdin.readline().strip()

def pow_two(n):
    ret = 0
    while n % 2 == 0:
        n //= 2
        ret += 1
    return ret

def main():
    n = int(input())
    A = list(map(int, input().split()))
    ans = 10**10
    for a in A: ans = min(ans, pow_two(a))
    print(ans)

if __name__ == "__main__":
    main()

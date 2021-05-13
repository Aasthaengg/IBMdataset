import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    s = list(input())
    t = list(input())
    ans = 0
    for a, b in zip(s, t):
        if a == b:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
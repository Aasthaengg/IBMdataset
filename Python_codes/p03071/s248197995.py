import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    a, b = map(int, input().split())
    ans = 0
    i = 0
    while i < 2:
        if a >= b:
            ans += a
            a -= 1
        else:
            ans += b
            b -= 1
        i += 1
    print(ans)
    
if __name__ == '__main__':
    main()
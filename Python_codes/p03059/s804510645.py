import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    a, b, t = map(int, input().split())
    ans = 0
    i = 1
    sec = 0
    while sec <= t+0.5:
        ans += b
        sec = a * i
        i += 1
    print(ans-b)
    
if __name__ == '__main__':
    main()
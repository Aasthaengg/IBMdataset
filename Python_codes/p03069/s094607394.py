import sys
input = sys.stdin.readline
 
 
def main():
    N = int(input())
    S = input().strip()
    ans = 0
    x = 0
    for c in S:
        if c == "#":
            x += 1
        else:
            if x > 0:
                ans += 1
                x = max(x-1, 0)
    print(ans)
 
 
if __name__ == '__main__':
    main()
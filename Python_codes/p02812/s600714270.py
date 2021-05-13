import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    s = list(input())
    ans = 0
    for i in range(n-2):
        if s[i] == 'A' and s[i+1] == 'B' and s[i+2] == 'C':
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
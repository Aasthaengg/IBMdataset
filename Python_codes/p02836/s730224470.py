import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    s = list(input())
    ans = 0
    for i in range(len(s)//2):
        if s[i] != s[-(i+1)]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
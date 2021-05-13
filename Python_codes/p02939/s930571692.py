import sys

input = sys.stdin.readline

def main():
    ans = 0
    S = input().rstrip('\n')
    p = t = ''
    for i in S:
        p += i
        if t != p:
            ans += 1
            p, t = '', p 
    print(ans)

if __name__ == '__main__':
    main()
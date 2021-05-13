import sys

input = sys.stdin.readline

def main():
    ans = 0
    n = int(input())
    s = input().rstrip('\n')
    t = input().rstrip('\n')
    for i in range(n):
        if s[i:] == t[:n-i]:
            print(n+i)
            break
    else:
        print(n*2)
        
if __name__ == '__main__':
    main()
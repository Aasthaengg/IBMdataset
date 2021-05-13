import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, k = map(int, input().split())
    s = list(input())
    s[k-1] = s[k-1].lower()
    print(*s, sep='')
    
if __name__ == '__main__':
    main()
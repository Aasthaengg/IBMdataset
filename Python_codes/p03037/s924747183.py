import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, m = map(int, input().split())
    L, R = 1, n
    for _ in range(m):
        l, m = map(int, input().split())
        if l > L: L = l
        if m < R: R = m
    print(max(0, R-L+1))
    
if __name__ == '__main__':
    main()
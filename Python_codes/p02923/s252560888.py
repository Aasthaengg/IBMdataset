import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    h = list(map(int, input().split()))
    compare = ''
    for i in range(n-1):
        if h[i] >= h[i+1]:
            compare += '1'
        else:
            compare += '0'
    print(max(list(map(len, compare.split('0')))))

if __name__ == '__main__':
    main()
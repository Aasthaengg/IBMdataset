import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    l = list(map(int, input().split()))
    l.sort(reverse=True)
    if l.pop(0) < sum(l):
        print('Yes')
    else:
        print('No')
        
if __name__ == '__main__':
    main()
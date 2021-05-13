import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    x = list(map(int, input().split()))
    print(len(set(x)))
    
if __name__ == '__main__':
    main()
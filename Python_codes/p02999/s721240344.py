import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    x, a = map(int, input().split())
    if x < a:
        print(0)
    else:
        print(10)
    
if __name__ == '__main__':
    main()
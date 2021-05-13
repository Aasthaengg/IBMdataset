import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = list(input().split())
    if len(n[0]) == 1 and len(n[1]) == 1:
        print(int(n[0])*int(n[1]))
    else:
        print(-1)
    
if __name__ == '__main__':
    main()
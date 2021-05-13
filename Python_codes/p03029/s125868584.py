import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    A, P = map(int, input().split())
    print((A * 3 + P) // 2)    

if __name__ == '__main__':
    main()

import sys
def input(): return sys.stdin.readline().rstrip()

def main():
    T, X = map(int, input().split())
    print(T / X)
    
if __name__ == '__main__':
    main()

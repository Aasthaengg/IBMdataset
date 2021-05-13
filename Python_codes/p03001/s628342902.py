import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    w, h, x, y = map(int, input().split())
    print(float(w)*float(h)/2, int(2*x == w and 2*y == h))
    
if __name__ == '__main__':
    main()
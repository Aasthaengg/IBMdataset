import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    h, w = map(int, input().split())
    dots = [input() for _ in range(h)]
    for i in dots:
        print(i, i, sep='\n')

if __name__ == '__main__':
    main()
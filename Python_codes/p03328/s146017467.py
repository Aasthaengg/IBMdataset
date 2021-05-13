import sys
input = sys.stdin.readline

def main():
    a, b = map(int, input().split())
    height = sum(list(range(b-a)))
    print(height - a)

if __name__ == '__main__':
    main()

import sys

def main():
    N, A, B = map(int, input().split())
    print('Alice' if (abs(A-B)-1)%2 != 0 else 'Borys')
if __name__ == '__main__':
    main()
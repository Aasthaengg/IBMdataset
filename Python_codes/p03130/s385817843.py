import sys
from collections import Counter
def main():
    read = sys.stdin.read
    A = map(int, read().split())
    c = Counter(A).most_common()[0][1]
    print('YES') if c == 2 else print('NO')

if __name__ == '__main__':
    main()

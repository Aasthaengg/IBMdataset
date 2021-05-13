import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from collections import Counter
def main():
    n = input()
    a = tuple(map(int, readlines()))
    ac = Counter(a)
    ac2 = [c % 2 for c in ac.values()]
    r = sum(ac2)
    print(r)
if __name__ == '__main__':
    main()

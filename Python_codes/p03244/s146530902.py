import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from collections import Counter 
def main():
    n = int(readline())
    a = [int(i) for i in readline().split()]
    odd = Counter(a[::2]).most_common(2)
    even = Counter(a[1::2]).most_common(2)
    odd.append((0, 0))
    even.append((0, 0))
    if odd[0][0] == even[0][0]:
        print(min(n-odd[1][1]-even[0][1], n-odd[0][1]-even[1][1]))
        return
    print(n-odd[0][1]-even[0][1])
if __name__ == '__main__':
    main()

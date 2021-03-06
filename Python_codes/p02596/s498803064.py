import sys
read = sys.stdin.read
#readlines = sys.stdin.readlines
from collections import defaultdict
def main():
    k = int(input())
    if k % 2 == 0:
        print(-1)
        sys.exit()
    rems = defaultdict(int)
    n = 7 % k
    next_digit = 70 % k
    r = 1
    while True:
        if n == 0:
            print(r)
            sys.exit()
        elif rems[n]:
            print(-1)
            sys.exit()
        else:
            rems[n] = 1
            n += next_digit
            n = n % k
            next_digit = (next_digit * 10) % k
            r += 1
if __name__ == '__main__':
    main()

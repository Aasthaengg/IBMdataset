import sys
import itertools
input = lambda: sys.stdin.readline().rstrip()

def main():
    l, r = map(int, input().split())
    if r - l >= 2018:
        print(0)
    else:
        ans = 2018
        for i, j in itertools.combinations(range(l, r+1), 2):
            ans = min(ans, i * j % 2019)
        print(ans)
    
if __name__ == '__main__':
    main()
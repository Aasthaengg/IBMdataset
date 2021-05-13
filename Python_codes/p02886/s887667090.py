import sys
import itertools
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    d = list(map(int,input().split()))
    ans = 0
    for i in itertools.combinations(d, 2):
        ans += i[0] * i[1]
    print(ans)

if __name__ == '__main__':
    main()
import sys
from collections import Counter
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    a = Counter(list(map(int, input().split())))
    
    ans = 0;
    for k, v in a.items():
        if k < v:
            ans += v - k
        elif k > v:
            ans += v
            
    print(ans)

if __name__ == '__main__':
    main()
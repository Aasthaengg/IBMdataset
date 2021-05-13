import sys
from collections import Counter
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = Counter(a)
    
    other = 0
    
    ans = n
    for k, v in a.items():
        ans -= v - 1
        if not v%2:
            other += 1
    
    ans -= other%2
        

    print(ans)
    
    
    
if __name__ == "__main__":
    main()

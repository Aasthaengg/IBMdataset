import sys
import math
import bisect

def main():
    p, q, r = map(int, input().split())
    ans = []
    ans.append(p + q)
    ans.append(q + r)
    ans.append(r + p)
    print(min(ans))
    
if __name__ == "__main__":
    main()

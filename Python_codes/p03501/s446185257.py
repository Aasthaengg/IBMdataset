import sys
import math
import bisect
 
def main():
    n, a, b = map(int, input().split())
    print(min(n * a, b))
 
if __name__ == "__main__":
    main()

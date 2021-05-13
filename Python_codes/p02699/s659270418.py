import sys
import math
import numpy as np
import copy

def main():
    s, w = map(int, input().split())
    print("unsafe" if s <= w else "safe")
    return 0

if __name__ == '__main__':
    sys.exit(main())
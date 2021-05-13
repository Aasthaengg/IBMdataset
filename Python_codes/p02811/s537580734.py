import math
from collections import deque
def main():
    t = [int(t)for t in input().split()]
    k,x = t[0],t[1]

    print("Yes" if 500*k >=x else "No")

if __name__ == "__main__":
    main()
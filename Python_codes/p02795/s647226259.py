import math
from collections import deque
def main():
    h = int(input())
    w = int(input())
    n = int(input())

    times = n//max([h,w])+(0 if n%max([h,w])==0 else 1)

    print(times)
if __name__ == "__main__":
    main()
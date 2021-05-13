from collections import defaultdict,deque
import math
def main():
    h,w=map(int, input().split())
    res = []
    for i in range(h):
        b=input()
        res.append(b)
        res.append(b)
    for i in res:
        print(i)
if __name__ == '__main__':
    main()

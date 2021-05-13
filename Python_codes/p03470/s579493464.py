from collections import defaultdict,deque
import math
def main():
    n = int(input())
    d = [int(input()) for i in range(n)]
    dd = defaultdict(int)
    for i in d:
        dd[i]+=1
    tmp = dd.keys()
    print(len(tmp))


if __name__ == '__main__':
    main()

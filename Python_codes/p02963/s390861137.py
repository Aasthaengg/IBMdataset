INF = 10 ** 9
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
from  heapq import heappop,heapify,heappush
from bisect import bisect_left

def main():
    s = int(input())
    a = int(s ** 0.5)
    while (a + 1) * (a + 1) <= s:
        a += 1

    b,c = 0,0
    flag = False
    while a <= INF:
        tmp = a * a - s
        if tmp == 0:
            b,c = 0,0
            break
        for i in range(1,tmp):
            if tmp%i == 0:
                j = tmp//i
                if i <= INF and j <= INF:
                    b = i
                    c = j
                    flag = True
                    break
        if flag:
            break
        else:
            a += 1
        
    print(0,0,a,c,b,a)
if __name__ == '__main__':
    main()

import bisect,collections,copy,heapq,itertools,math,string
import sys
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
h = LIST()
mh = max(h)
cnt = 0
for i in range(1,mh+1):
    for j in range(n):
        if j == 0:
            flag = cnt_area = 1 if h[j] >= i else 0
        elif flag == 0 and h[j] >= i:
            flag = 1
            cnt_area += 1
        else:
            flag = (h[j] >= i)
    cnt += cnt_area

print(cnt)
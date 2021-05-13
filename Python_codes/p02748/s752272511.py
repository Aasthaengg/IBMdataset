import heapq
from sys import stdin
input = stdin.readline

#入力
# s = list(input()[0:-1])
# n = int(input())
A,B,M = map(int, input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
# w = [int(input()) for i in range(n)]

xyc=[]
for i in range(M):
    x,y,c = map(int, input().split())
    xyc.append((x,y,c))
     
def main():
    mn = sorted(a)[0]+sorted(b)[0]
    for x, y, c in xyc:
        mn = min(mn, a[x-1]+b[y-1] - c)

    print(mn)
        
if __name__ == '__main__':
    main()
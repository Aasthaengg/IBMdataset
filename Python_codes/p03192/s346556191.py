import heapq
from sys import stdin
input = stdin.readline

#入力
# s = list(input()[0:-1])
# n = int(input())
# A,B,M = map(int, input().split())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# w = [int(input()) for i in range(n)]

# xyc=[]
# for i in range(M):
#     x,y,c = map(int, input().split())
#     xyc.append((x,y,c))
def main():
    n = int(input())
    ans = 0
    while n >0:
        if n %10 == 2:
            ans += 1
        n= n//10
    print(ans)
if __name__ == '__main__':
    main()
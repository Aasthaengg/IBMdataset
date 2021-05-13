import heapq
from sys import stdin
input = stdin.readline

#入力
# s = list(input()[0:-1])
# n = int(input())
# A,B,M = map(int, input().split())
a = list(map(int,input().split()))
a = sorted(a)
# b = list(map(int,input().split()))
# w = [int(input()) for i in range(n)]

# xyc=[]
# for i in range(M):
#     x,y,c = map(int, input().split())
#     xyc.append((x,y,c))
     
def main():

    if a[0]==1 and a[1]==4 and a[2]==7 and a[3]==9:
        print("YES")
    else:
        print("NO")

        
if __name__ == '__main__':
    main()
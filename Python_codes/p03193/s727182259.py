import heapq
from sys import stdin
input = stdin.readline

#入力
# s = list(input()[0:-1])
# n = int(input())
N,H,W = map(int, input().split())
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# w = [int(input()) for i in range(n)]

ab=[]
for i in range(N):
    a,b = map(int, input().split())
    ab.append((a,b))
def main():
    ans = 0 
    for a,b in ab:
        if a>=H and b >=W:
            ans+=1
    print(ans)
    
if __name__ == '__main__':
    main()
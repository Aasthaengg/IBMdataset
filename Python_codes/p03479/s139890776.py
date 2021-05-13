import heapq
from sys import stdin
input = stdin.readline

#入力
# s = input()
# n = int(input())
# a,b = map(int, input().split())
# a = list(map(int,input().split()))
# w = [int(input()) for i in range(n)]

# ab=[]
# for i in range(m):
#     a,b = map(int, input().split())
#     ab.append((a,b))
     
def main():
    a,b = map(int, input().split())
    ans = 0
    while a <=b:
        ans+=1
        a*=2
    print(ans)
        
if __name__ == '__main__':
    main()
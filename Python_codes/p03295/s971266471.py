import heapq
from sys import stdin
input = stdin.readline

#入力
# s = input()
# n = int(input())
n,m = map(int, input().split())
# a = list(map(int,input().split()))
# a = [int(input()) for i in range()]

ab=[]
for i in range(m):
    a,b = map(int, input().split())
    ab.append((a,b))
ab = sorted(ab, key = lambda x: x[1])

     
def main():
    left = 0
    ans = 0
    for a,b in ab:

        if left < a:
            left = b-1
            ans +=1
    print(ans)


    
    

if __name__ == '__main__':
    main()
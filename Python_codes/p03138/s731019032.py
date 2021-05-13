from collections import Counter,defaultdict,deque
import sys
from itertools import permutations, combinations
from heapq import heappop, heappush
# input = sys.stdin.readline
sys.setrecursionlimit(10**8)
# mod = 10**9+7
    
def inp(): # n=1
    return int(input())
def inpm(): # x=1,y=2
    return map(int,input().split())
def inpl(): # a=[1,2,3,4,5,...,n]
    return list(map(int, input().split()))
def inpls(): # a=['1','2','3',...,'n']
    return list(input().split())
def inplm(n): # x=[] 複数行
    return list(int(input()) for _ in range(n))
def inpll(n): # [[1,1,1,1],[2,2,2,2],[3,3,3,3]]
    return sorted([list(map(int, input().split())) for _ in range(n)])

def main():
    n,k = inpm()
    a = inpl()
    x = [0 for _ in range(41)]
    y = [0 for _ in range(41)]
    index = 0
    while k > 0:
        x[index] += k%2
        k //= 2
        index += 1
    for i in range(n):
        index = 0
        while a[i] > 0:
            y[index] += a[i]%2
            a[i] //= 2
            index += 1
    ans = 0
    key1 = 0
    key2 = 0
    for i in range(40,-1,-1):
        flag = (y[i]>=(n/2))
        if x[i]>0 or y[i]>0:
            key2 = 1
        if x[i] == 1 and flag and key2 and (not key1):
            key1 = True
            ans += pow(2,i)*y[i]
        elif key2:
            if flag or (x[i] == 0 and (not key1)):
                ans += pow(2,i)*y[i]
            else:
                ans += pow(2,i)*(n-y[i])
    print(ans)

if __name__ == "__main__":
    main()
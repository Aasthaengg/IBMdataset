import sys
INF = 10 ** 11
MOD = 10 ** 9 + 7
from collections import deque
sys.setrecursionlimit(100000000)
from heapq import heapify,heappush,heappop   

def main():
    n = int(input())
    a = list(map(int,input().split()))
    m = []
    p = []
    z = 0
    for num in a:
        if num < 0:
            m.append(num)
        elif num > 0:
            p.append(num)
        else:
            z += 1
    
    ans = []
    
    if z == n:
        print(0)
        for i in range(n - 1):
            print(0,0)
        return

    if len(p) == 0:
        if z:
            num1 = 0
            z -= 1
        else:
            m.sort()
            num1 = m[-1]
            m.pop()
        for i in range(len(m)):
            ans.append((num1,m[i]))
            num1 -= m[i]
    
    elif len(m) == 0:
        if z:
            num1 = 0
            z -= 1
            idx = 0
        else:
            p.sort()
            num1 = p[0]
            idx = 1
        for i in range(idx,len(p) - 1):
            ans.append((num1,p[i]))
            num1 -= p[i]
        ans.append((p[-1],num1))
        num1 = p[-1] - num1
    
    elif len(p) * len(m) > 0:
        num1 = p[-1]
        p.pop()
        num2 = m[-1]
        m.pop()
        for i in range(len(m)):
            ans.append((num1,m[i]))
            num1 -= m[i]
        for i in range(len(p)):
            ans.append((num2,p[i]))
            num2 -= p[i]
        ans.append((num1,num2))
        num1 -= num2
    
    for i in range(z):
        ans.append((num1,0))
    print(num1)
    for i in range(n - 1):
        print(*ans[i])

if __name__=='__main__':
    main()
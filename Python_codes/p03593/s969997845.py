import sys
INF = 10 ** 9
MOD = 10 ** 9 + 7
from collections import deque
sys.setrecursionlimit(100000000)
from math import sin,pi

def main():
    h,w = map(int,input().split())
    dic = {}
    for _ in range(h):
        a = list(input())
        for s in a:
            if s in dic:
                dic[s] += 1
            else:
                dic[s] = 1
    
    ans = 'Yes'
    if h%2 == 0 and w%2 == 0:
        for v in dic.values():
            if v%4 != 0:
                ans = 'No'
                cnt = 0
                break
    
    elif h%2 == 0:
        cnt = 0
        for v in dic.values():
            if v%4 == 0:
                cnt += cnt//4
            elif v%2 == 0:
                cnt += (v - 2)//4
            else:
                ans = 'No'
                cnt = 0
                break
        
        if cnt < (h//2) * (w//2):
            ans = 'No'
    
    elif w%2 == 0:
        cnt = 0
        for v in dic.values():
            if v%4 == 0:
                cnt += v//4
            elif v%2 == 0:
                cnt += (v - 2)//4
            else:
                ans = 'No'
                cnt = 0
                break
        
        if cnt < (h//2) * (w//2):
            ans = 'No'
    
    else:
        cnt = 0
        flag = False
        for v in dic.values():
            if v%4 == 0:
                cnt += v//4
            elif v%2 == 0:
                cnt += (v - 2)//4
            else:
                if flag:
                    ans = 'No'
                    cnt = 0
                    break
                flag = True
                v -= 1
                if v%4 == 0:
                    cnt += v//4
                else:
                    cnt += (v - 2)//4
        if cnt < (h//2) * (w//2):
            ans = 'No'
    
    print(ans)
if __name__=='__main__':
    main()
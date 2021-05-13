import sys
INF = 10 ** 9
MOD = 10 ** 9 + 7
from collections import deque
sys.setrecursionlimit(100000000)

def main():
    s = list(input())
    
    cnt = 0
    ans = 0
    if len(s) < 3:
        print(0)
        exit()

    i = len(s) - 1
    while i > 0:
        while i > 0 and s[i-1] == 'B' and s[i] == 'C':
            cnt += 1
            i -= 2  
            while i >= 0 and s[i] == 'A':
                ans += cnt
                i -= 1
        else:
            cnt = 0
            i -= 1

    print(ans)
if __name__=='__main__':
    main()

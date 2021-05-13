INF = 10 ** 9
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
from  collections import deque

def main():
    s = list(input())
    k = int(input())
    for i in range(len(s)):
        if s[i] == 'a':
            continue
        if k >= ord('z') - ord(s[i]) + 1:
            k -= ord('z') - ord(s[i]) + 1
            s[i] = 'a'
            if k == 0:
                break
    
    if k > 0:
        s[-1] = chr((ord(s[-1]) + k - 97)%26 + 97)
    
    print(''.join(s))
if __name__ == '__main__':
    main()

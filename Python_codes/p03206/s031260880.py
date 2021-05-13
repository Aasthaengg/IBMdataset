import sys
INF = 10 ** 10
MOD = 10 ** 9 + 7
from collections import deque

def main():
    d = int(input())
    ans = ['Christmas']
    for i in range(d,25):
        ans.append('Eve')
    print(' '.join(ans))
if __name__ =='__main__':
    main()    
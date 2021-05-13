INF = 10 ** 9
MOD = 10 ** 9 + 7
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)
from  math import factorial


def main():
    s = input()
    K = 'keyence'
    if s[:7] == K or s[-7:] == K:
        print('YES')
        return
    ans = 'NO'
    for i in range(7):
        a = K[:i]
        b = K[i:]
        if s[:i] == a and s[-7+i:] == b:
            ans = 'YES'
            break
    print(ans)
if __name__ == '__main__':
    main() 
MOD = 10 ** 9 + 7
INF = 10 ** 10
import sys
sys.setrecursionlimit(100000000)
dy = (-1,0,1,0)
dx = (0,1,0,-1)

def main():
    a = input()
    dic = {}
    for s in a:
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
    
    ans = 0
    n = len(a)
    for v in dic.values():
        ans += v * (n - v)
    ans = ans//2 + 1
    print(ans)
if __name__ =='__main__':
    main()  
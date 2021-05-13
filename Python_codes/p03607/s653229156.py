import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n = I()
    dic = collections.defaultdict(int)
    ans = 0
    for _ in range(n):
        a = I()
        dic[a] += 1
    for key,value in dic.items():
        if value%2 == 1:
            ans += 1
    print(ans)
main()            

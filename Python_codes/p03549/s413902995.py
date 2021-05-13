import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    n, m = LI()
    ans_ip = 0
    unit = (1/2)**m

    for i in range(1,10**5):
        p = (1-unit)**(i-1)*(unit)
        ans_ip+= i*p
    t = (n-m)*100 + m*1900

    ans= t*ans_ip
    ans = round(ans)
    print(ans)
main()

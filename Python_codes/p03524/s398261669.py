import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():
    s = S()
    count = collections.Counter(s)
    lst = list(count.values())
    while len(lst)<3:
        lst.append(0)
    m = min(lst)
    lst = list(map(lambda x: x-m, lst))
    if max(lst)<=1:
        print("YES")
    else:
        print("NO")
main()

import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip.split())
def main():
    n = I()
    dic = collections.defaultdict(lambda : ":(")
    for i in range(1,46300):
        tax = i*108//100
        dic[tax] = i
    print(dic[n])
main()
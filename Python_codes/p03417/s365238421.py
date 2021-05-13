#import collections
#aa = collections.Counter(a) # list to list
#from itertools import combinations # (string,3) 3回

mod = 10**9 + 7

def readInts():
  return list(map(int,input().split()))
def main():
    n,m = readInts()
    """
    N <= M
    N = 1かつ、M = 1のとき、1枚だけあるカードは1毎裏返されるので、答えは1でｓ。
    N = 1かつ M ≠ 1のとき、 M 枚のカードのうち両端のカードは2回、それ以外のカードは
    3回裏替えされるので、答えはM-2
    N >= 2のとき、 N <= M より M >= 2で、このとき、
    ・四隅のカードは4回、　# 表になる
    ・それ以外のカードは週上のカードは6回 # 表になる
    ・それ以外のカードは9回
    裏返されるので、答えは、(N-2)(M-2)
    """

    if n == 1 and m == 1:
        print(1)
    elif n == 1 and m != 1:
        print(m-2)
    elif m == 1 and n != 1:
        print(n-2)
    else:
        print((n-2) * (m-2))
if __name__ == '__main__':
  main()

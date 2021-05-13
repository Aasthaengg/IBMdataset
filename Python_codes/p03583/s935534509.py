#Tenka1 Programmer Contest-C 4/N
"""
nが与えられるので、
4/n = 1/a + 1/b + 1/c　となるa,b,cを出力せよ
なお、a,b,c<=3500となる中で1つは解があることが保証される。

多分半分全列挙のような解法になると思う

"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n = int(readline())
flag = 0
for a in range(1,3501):
    for b in range(1,3501):
        try:
            c = int(a*b*n/(4*a*b-n*b-n*a))
            if c<0:
                continue
            if 4*a*b*c//(b*c+c*a+a*b)==n:
                print(a,b,c)
                flag = 1
        except:
            pass
        if flag:
            exit()

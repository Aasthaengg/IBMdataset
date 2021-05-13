# coding: utf-8
# Your code here!
# coding: utf-8
from fractions import gcd 
from functools import reduce
import sys
sys.setrecursionlimit(200000000)
from inspect import currentframe


# my functions here!
#標準エラー出力
def printargs2err(*args):
    names = {id(v):k for k,v in currentframe().f_back.f_locals.items()}
    print(', '.join(names.get(id(arg),'???')+' : '+repr(arg) for arg in args),file=sys.stderr)
def debug(*args):
    print(*args,file=sys.stderr)

def printglobals():
    for (symbol, value) in globals().items():
        print('symbol="%s"、value=%s' % (symbol, value),file=sys.stderr)
def printlocals():
    for (symbol, value) in locals().items():
        print('symbol="%s"、value=%s' % (symbol, value),file=sys.stderr)
#入力（後でいじる）
def pin(type=int):
    return map(type,input().split())
     
#input

                
def resolve():
    N=int(input())
    b=list(pin())
    ans=[]
    t=0
    for elem in range(N):
        for i in range(N-t,0,-1):
            if b[i-1]==i:
                ans.append(i)
                b.pop(i-1)
                t+=1
                break
    if len(ans)!=N:print("-1")
    else:
        for wa in reversed(ans):
            print(wa)
        #print([["NA","YYMM"],["MMYY","AMBIGUOUS"]][cMMYY][cYYMM])
#if __name__=="__main__":resolve()

"""
#printデバッグ消した？
#前の問題の結果見てないのに次の問題に行くの？
"""
"""
お前カッコ閉じるの忘れてるだろ
"""
import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """3
1 2 1"""
        output = """1
1
2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2
2 2"""
        output = """-1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """9
1 1 1 2 2 1 2 3 2"""
        output = """1
2
2
3
1
2
2
1
1"""
        self.assertIO(input, output)

if __name__=="__main__":resolve()
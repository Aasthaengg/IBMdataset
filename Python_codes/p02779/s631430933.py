from collections import Counter as Ct
INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))

def do():
    n=INT()
    a=LIST()
    a=set(a)
    if n==len(a):
        print('YES')
    else:
        print('NO')
if __name__=='__main__':
    do()
INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))
def do():
    a,b,c,d=INTM()
    if (a-d<=c<=a+d) or (a-d<=b<=a+d and c-d<=b<=c+d):
        print('Yes')
    else:
        print('No')
if __name__ == '__main__':
    do()
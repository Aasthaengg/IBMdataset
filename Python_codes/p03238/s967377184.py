INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))
def do():
    n=INT()
    if n==1:
        print('Hello World')
    else:
        a=INT()
        b=INT()
        print(a+b)
if __name__ == '__main__':
    do()
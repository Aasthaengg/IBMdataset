INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))
def do():
    x,a=INTM()
    if x<a:
        print(0)
    else:
        print(10)
if __name__ == '__main__':
    do()
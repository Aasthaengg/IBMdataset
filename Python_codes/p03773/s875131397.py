INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
def do():
    a,b=INTM()
    print((a+b)%24)
if __name__ == '__main__':
    do()
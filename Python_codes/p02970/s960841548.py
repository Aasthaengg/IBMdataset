INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))
def do():
    n,d=INTM()
    print(int((n+(d*2+0.9))//(d*2+1)))
if __name__ == '__main__':
    do()
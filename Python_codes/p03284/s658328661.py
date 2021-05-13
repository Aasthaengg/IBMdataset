INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))
def do():
    n,k=INTM()
    if n%k==0:
        print(0)
    else:
        print(1)
if __name__ == '__main__':
    do()
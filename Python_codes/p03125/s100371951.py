INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))
def do():
    a,b=INTM()
    if b%a==0:
        print(a+b)
    else:
        print(b-a)
if __name__ == '__main__':
    do()
INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))
def do():
    a,b,c=INTM()
    if a==b:
        print(c)
    elif a==c:
        print(b)
    else:
        print(a)
if __name__ == '__main__':
    do()
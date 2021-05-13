INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
def do():
    a,b,c = INTM()
    if (a+c)/2 == b:
        print('YES')
    else:
        print('NO')
if __name__ == '__main__':
    do()
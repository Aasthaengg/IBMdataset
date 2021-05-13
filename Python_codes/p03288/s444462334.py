INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))
def do():
    r=INT()
    if r<1200:
        print('ABC')
    elif r<2800:
        print('ARC')
    else:
        print('AGC')
if __name__ == '__main__':
    do()
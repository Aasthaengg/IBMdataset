INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))
def do():
    a=INT()
    s=STR()
    if a<3200:
        print('red')
    else:
        print(s)
if __name__ == '__main__':
    do()
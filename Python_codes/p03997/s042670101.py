INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
def do():
    a = INT()
    b = INT()
    h = INT()
    print(int((a+b)*h/2))
if __name__ == '__main__':
    do()
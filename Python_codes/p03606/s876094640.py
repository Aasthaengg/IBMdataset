INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))
def do():
    n=INT()
    ans=0
    for i in range(n):
        l,r=INTM()
        ans+=r-l+1
    print(ans)
if __name__ == '__main__':
    do()
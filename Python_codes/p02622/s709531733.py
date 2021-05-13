INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))
def do(): 
    s=STR()
    t=STR()
    ct=0
    for i in range(len(s)):
        if s[i]!=t[i]:
            ct+=1
    print(ct)


if __name__ == '__main__':
    do()
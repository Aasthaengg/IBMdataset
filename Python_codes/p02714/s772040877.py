INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))
def do():
    n=INT()
    s=STR()
    r=s.count('R')
    g=s.count('G')
    b=s.count('B')
    ans=r*g*b
    #print(ans)
    for i in range(n+1):
        for j in range(1,n//2+2):
            k=i+2*j
            if k<=n-1:
                #print(ch)
                if (s[i]!=s[i+j] and s[k]!=s[i+j] and s[i]!=s[k]):
                    ans-=1
                    
    print(ans)

                
if __name__ == '__main__':
    do()
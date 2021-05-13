
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    S=input()
    a=S.count("a")
    b=S.count("b")
    c=S.count("c")
    
    aa=max(a,b,c)
    cc=min(a,b,c)
    bb=a+b+c-aa-cc
    
    pre="e"
    now="d"
    
    N=len(S)
    for i in range(N):
        if now!="a" and pre!="a":
            aa-=1
            pre=now
            now="a"
        elif now!="b" and pre!="b":
            bb-=1
            pre=now
            now="b"
        else:
            cc-=1
            pre=now
            now="c"
            
    if (aa,bb,cc) == (0,0,0):
        print("YES")
    else:
        print("NO")

main()

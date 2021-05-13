import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())
def NIJIGEN(H): return [list(input()) for i in range(H)]
a,b,c,d=MAP()
x=c-a
y=d-b
ans=str()
ans+="R"*x+"U"*y
ans+="L"*x+"D"*y
ans+="L"+"U"*(y+1)+"R"*(x+1)+"D"
ans+="R"+"D"*(y+1)+"L"*(x+1)+"U"
print(ans)
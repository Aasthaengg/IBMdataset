a,b,x=map(int,input().split())
#a<=y<=bでy%x=0を満たすyの個数を求める
#f(n)を0以上n以下で上記のyの個数を表す関数と定義する
#すると，問題の答えはf(b)-f(a-1)である
#f(b):0以上b以下のyの個数,f(a-1):0以上a-1以下のyの個数
#a=0のときf(-1)が呼ばれることに注意する
#f(b)=b//x+1
#a>0 f(a-1)=(a-1)//x+1
#a=0 f(a-1)=0
def between(a,b,x):
    if a==0:
        na=0
    else:
        na=(a-1)//x+1
    nb=b//x+1
    print(nb-na)
between(a,b,x)
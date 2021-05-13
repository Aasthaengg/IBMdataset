S,C=map(int,input().split())

x=min(S, C//2)
if S>x:
    print(x)
else:
    x+=(C-2*x)//4
    print(x)
A,B=map(int,input().split())

ans=A+B
if ans>=24:
    ans = ans - 24

print(ans)
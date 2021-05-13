A,B,C,D=map(int,input().split())
s=A*B
t=C*D
if s==t:
    print(s)
else:
    print(max(s,t))
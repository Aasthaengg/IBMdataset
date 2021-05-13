A,B=map(int,input().split())
max=A+B
if max<A-B:
    max=A-B
if max<A*B:
    max=A*B
print(max)
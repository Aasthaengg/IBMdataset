n=int(input())
mina=0
minb=0
for i in range(n):
    a,b=map(int,input().split())
    if mina<a:
        mina=a
        minb=b
print(mina+minb)

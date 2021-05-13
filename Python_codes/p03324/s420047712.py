import sys
sys.setrecursionlimit(10**6)

d,n=map(int,input().split())

if d==0:
    if n==100:
        print(n+1)
        exit()
    print(n)
elif d!=0 and n==100:
    print((n+1)*100**d)
else:
    print(n*100**d)

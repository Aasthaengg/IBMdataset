from sys import exit

ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

r,d,x = mi()
ans=x
for i in range(10):
    ans = r*ans - d
    print(ans)
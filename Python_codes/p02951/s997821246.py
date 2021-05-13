ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

a,b,c = mi()
ans = c - (a-b)
if ans < 0:
    print(0)
else:
    print(ans)
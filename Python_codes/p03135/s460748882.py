ii = lambda:int(input())
mi = lambda:list(map(int,input().split()))
ix = lambda x:list(input() for _ in range(x))
mix = lambda x:list(mi() for _ in range(x))
iix = lambda x:list(int(input()) for _ in range(x))
##########

t,x = mi()
print(t/x)
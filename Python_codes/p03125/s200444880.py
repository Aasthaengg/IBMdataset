ii = lambda:int(input())
mi = lambda:list(map(int,input().split()))
ix = lambda x:list(input() for _ in range(x))
mix = lambda x:list(mi() for _ in range(x))
iix = lambda x:list(int(input()) for _ in range(x))
##########
def main(a,b):
    return a + b if b % a == 0 else b - a

a,b = mi()
print(main(a,b))
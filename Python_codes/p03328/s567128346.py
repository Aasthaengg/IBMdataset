import sys
sys.setrecursionlimit(10 ** 9)

a,b = map(int,input().split())
d = b-a

def h(x:int):
    if x == 1:
        return 1
    else:
        return h(x-1)+x

print (h(d)-b)

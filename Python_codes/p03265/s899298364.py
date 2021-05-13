import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

a,b,c,d = MI()
e,f = c-a,d-b
print(c-f,d+e,a-f,b+e)

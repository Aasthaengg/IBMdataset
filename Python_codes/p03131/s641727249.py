import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

k,a,b = MI()

if a+2 >= b:
    print(1+k)
elif a >= k+2:
    print(1+k)
elif (k-a+1)%2 == 0:
    print((k-a+1)//2*(b-a)+a)
else:
    print((k-a+1)//2*(b-a)+a+1)

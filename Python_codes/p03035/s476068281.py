import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

a,b=MI()
if a>=13:
    price=b
elif 6<=a<=12:
    price=int(b/2)
else:
    price=0
print(price)
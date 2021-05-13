def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
mod=10**9+7

a,b,c,d=MI()

l=a+b
r=c+d

if l>r:
    print("Left")
elif r>l:
    print("Right")
else:
    print("Balanced")



#from fractions import gcd
#mod = 10 ** 9 + 7
#N = int(input())
#a = list(map(int,input().split()))
#a,b,c = map(int,input().split())
#ans = [0] * N

def intinput():
    return int(input())

def listintinput():
    return list(map(int,input().split()))

N = intinput()
a = listintinput()
print(max(a)-min(a))

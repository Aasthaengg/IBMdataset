#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))

n,d = map(int, input().split())

if (n%(2*d+1) == 0):
    print( n // (2*d+1))
else:
    print( n // (2*d+1) + 1)

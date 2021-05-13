ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

a,b,c,d = mi()

l = [a*c,a*d,b*c,b*d]

print(max(l))
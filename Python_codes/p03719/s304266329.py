from sys import exit

ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

a,b,c = mi()
if a <= c and c <= b:
    print("Yes")
else:
    print("No")
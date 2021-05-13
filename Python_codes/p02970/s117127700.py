a,b = map(int,input().split())

r = b*2+1

if a%r == 0:
    print(a//r)
else:
    print(a//r+1)

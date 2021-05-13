import sys
stdin=sys.stdin

ip=lambda: int(sp())
lp=lambda:list(map(int,stdin.readline().split()))
sp=lambda:stdin.readline().rstrip()

a,b,c=input().split(',')

print(a+' '+b+' '+c)



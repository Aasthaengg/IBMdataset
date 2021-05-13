n,a,b = map(int,input().split())

if n>=(a+b):
    MAX = min(a,b)
    MIN = 0
else:
    MAX = min(a,b)
    MIN = a+b-n

print(str(MAX)+' '+str(MIN))
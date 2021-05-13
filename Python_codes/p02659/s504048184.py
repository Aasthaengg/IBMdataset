a,b = map(str,input().split())
#print(b[:-3]+b[-2:])
tmp = int(a) * int(b[:-3]+b[-2:])
print(tmp//100)
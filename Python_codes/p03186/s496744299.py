a,b,c = map(int, input().split())
if a+b<c: print(b*2+a+1)
elif a+b==c: print(b*2+a)
else: print(b+c)
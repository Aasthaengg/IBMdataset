a , b = map(int,input().split())
x = (a+b) / 2
print(int(x) if x.is_integer() else 'IMPOSSIBLE' )

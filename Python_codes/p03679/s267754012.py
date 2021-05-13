x,a,b = list(map(int,input().split()))

if b <= a:
    result = 'delicious'
elif b <= a+x:
    result = 'safe'
else:
    result = 'dangerous'
print(result)
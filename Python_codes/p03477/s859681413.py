a,b,c,d = map(int,input().split())
i = a + b
j = c + d
if i < j:
    print('Right')
elif i > j:
    print('Left')
else:
    print('Balanced')
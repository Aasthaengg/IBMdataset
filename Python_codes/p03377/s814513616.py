a, b, x = map(int, input().split())
sum = a+b
if x-a > b:
    print('NO')
    
elif a > x:
    print('NO')

else:
    print('YES')
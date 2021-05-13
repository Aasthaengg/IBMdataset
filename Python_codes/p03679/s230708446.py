
x, a, b= list(map(int, input().split()))

if a >= b:
    print("delicious")
elif a < b and x >= b-a:
    print('safe')
else:
    print('dangerous')
arr = input().split()
x = int(arr[0])
a = int(arr[1])
b = int(arr[2])

if b <= a:
    print('delicious')
elif b - a <= x:
    print('safe')
elif b - a >= x + 1:
    print('dangerous')

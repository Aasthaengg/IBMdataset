arr = input().split()
arr = list(map(str,arr))
a = arr[0]
b = arr[1]
if a == 'H' and b == 'H':
    print('H')
elif a == 'D' and b == 'H':
    print('D')
elif a == 'D' and b == 'D':
    print('H')
elif a == 'H' and b == 'D':
    print('D')

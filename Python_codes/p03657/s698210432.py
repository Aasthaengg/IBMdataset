arr = input().split()
arr = list(map(int,arr))
a = arr[0]
b = arr[1]

if a % 3 == 0 or b % 3 == 0 or (a+b) % 3 == 0:
    print('Possible')
else:
    print('Impossible')

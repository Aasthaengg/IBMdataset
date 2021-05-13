sheet = input().split()
sheet_i = [int(s) for s in sheet]
a, b = sheet_i

if(a % 3 == 0 or b % 3 == 0):
    print('Possible')
elif((a+b) % 3 == 0):
    print('Possible')
else:
    print('Impossible')

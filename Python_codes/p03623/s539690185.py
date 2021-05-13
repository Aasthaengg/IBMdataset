num = input().split()

if abs(int(num[0])-int(num[1])) < abs(int(num[0])-int(num[2])): print('A')
else: print('B')
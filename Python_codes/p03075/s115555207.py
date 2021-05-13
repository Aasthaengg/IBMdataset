import sys
a = [int(input()) for _ in range(6)]

for i in a[1:-1]:
    if i-a[0] > a[-1]:
        print(':(')
        sys.exit()
print('Yay!')

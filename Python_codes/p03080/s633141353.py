n = int(input())
s = input()
red = len(s.replace('B', ''))
blue = n - red
if red > blue:
    print('Yes')
else:
    print('No')
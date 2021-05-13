N = int(input())
s = input()

red = s.count('R')
blue = s.count('B')

if red > blue:
    print('Yes')
else:
    print('No')

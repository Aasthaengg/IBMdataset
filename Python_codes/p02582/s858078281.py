S = input()
n = S.count('R')

if n == 2:
    if S == 'RSR':
        print(1)
    else:
        print(2)
else:
    print(n)
n = int(input())
s = list(input().split())
arare = len(set(s))

if arare == 4:
    print('Four')
else:
    print('Three')

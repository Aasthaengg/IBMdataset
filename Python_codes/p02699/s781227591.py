from sys import exit

S, W = [int(x) for x in input().split()]

if S > W:
    print('safe')
    exit()

print('unsafe')

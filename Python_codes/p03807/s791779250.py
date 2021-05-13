n = int(input())
a = len([i for i in input().split() if int(i)%2 == 1])
if a%2 == 0: print('YES')
else: print('NO')


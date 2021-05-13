a, b = map(int, input().split())
M = [['#']*100 for _ in range(50)] + [['.']*100 for _ in range(50)]

for i in range(a-1):
    M[(2*i//100)*2][2*i%100] = '.'

for i in range(b-1):
    M[99 - (2*i//100)*2][2*i%100] = '#'

print(100, 100) 
for l in M:
    print(''.join(l))
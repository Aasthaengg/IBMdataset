n, T = map(int, input().split())

index = -1
min_c = 9999
for i in range(n):
    c, t = map(int, input().split())
    # print(f'{c} {t}')
    
    if t <= T and min_c > c:
        index = i + 1
        min_c = c
    # print(min_c)
        
if index == -1:
    print('TLE')
else:
    print(min_c)
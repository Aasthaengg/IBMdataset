n = int(input())
s = list(map(str, input().split()))
f = [False] * 4
for i in range(n):
    if s[i] == 'P':
        f[0] = True

    elif s[i] == 'W':
        f[1] = True
    
    elif s[i] == 'G':
        f[2] = True
    
    else:
        f[3] = True

if sum(f) == 3:
    print('Three')

elif sum(f) == 4:
    print('Four')
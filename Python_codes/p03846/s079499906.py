n = int(input())
a = [int(i) for i in input().split()]
s = 0
b = 0
d = [0]*n
if n % 2 == 0:
    for i in a:
        d[i] += 1 
    for i in range(1,n,2):
        if d[i] != 2:
            s = 1
            break
        else:
            b += 1
    ans = 2 ** b % (10**9 + 7)
else:
    for i in a:
        d[i] += 1 
    
    for i in range(0,n,2):
        if i == 0 and d[0] == 1:
            ans = 1
        elif d[i] != 2:
            s = 1
            break
        else:
            b += 1
    ans = 2 ** (b) % (10**9 + 7)

if s == 0:
    print(ans)
elif s == 1:
    print('0')
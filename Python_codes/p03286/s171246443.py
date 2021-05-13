import sys
n = int(input())
if n == 0:
    print(0)
    sys.exit()
ans = []
while n != 0:
    if n < 0:
        r = n % -2
        n = -(-n//-2)
        if r < 0:
            r *= -1
    else:
        r = n%2
        n = n//2
        n *= -1 
    ans.append(str(r))
ans = ans[::-1]
print(''.join(ans))
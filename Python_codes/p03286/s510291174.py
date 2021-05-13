n = int(input())
ans = ''
while n!=0:
    bit = '0'
    if n%2:
        n -= 1
        bit = '1'
    ans = bit + ans
    n//=-2
if ans == '': ans = '0'
print(ans)

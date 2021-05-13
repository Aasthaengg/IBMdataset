n = int(input())
num = len(str(n))
if num == 1:
    ans = n
else:
    if num&1==1:
        ans = (n%(10**(num-1)))+1+(n//(10**(num-1))-1)*(10**(num-1))
        num -=2
    else:
        ans = 0
        num -= 1
    n %= 10**num
    while num>0:
        ans += 9*(10**(num-1))
        num -=2
        n %= 10**num
print(ans)
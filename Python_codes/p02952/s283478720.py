
def odd(x):
    if (x-1)%2 == 0:
        return True
    else:
        return False


N = input()
index, num = len(N), int(N)

ans = 0
for i in range(1, index+1):
    if odd(i):
        if num >= 10**i:
            ans = ans + (10**i - 10**(i-1))
            
        else:
            ans = ans + (num - 10**(i-1) + 1)
            
print(ans)
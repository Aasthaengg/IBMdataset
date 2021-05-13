n = int(input())
ans = ''
p = -2
while n!=0:
    n,r = divmod(n,p)
    if r < 0:
        r -= p
        n += 1
    ans = str(r) + ans
if ans == '': ans = '0'
print(ans)

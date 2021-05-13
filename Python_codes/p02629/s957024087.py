n = int(input())

abc = 'abcdefghijklmnopqrstuvwxyz'
ans = ''
while n:
    n -= 1
    n, m = divmod(n, 26)
    ans = abc[m] + ans
print(ans)
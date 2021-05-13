N = int(input())
s = 'abcdefghijklmnopqrstuvwxyz'
ans = ''
while N>0:
    N -= 1
    ans = s[N%26] + ans
    N = N // 26
print(ans)
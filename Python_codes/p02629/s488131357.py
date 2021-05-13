n=int(input())
ans = ''
while n>0:
        n = n-1
        ans += chr(ord('a') + (n)% 26)
        n//=26
ans = ans[::-1]
print(ans)
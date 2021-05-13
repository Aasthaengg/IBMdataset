n=int(input())
s='abcdefghijklmnopqrstuvwxyz'

ans=''
while n > 0:
    n=n-1
    ans+=s[n%26]
    n=n//26

print(ans[::-1])
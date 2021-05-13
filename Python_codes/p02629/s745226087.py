n=int(input())
c=""
while n:
    n-=1
    c=chr(n%26+97)+c
    n//=26
print(c)
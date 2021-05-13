n=int(input())

ans=""
while n>0:
    n -=1
    n,b=divmod(n,26)
    ans +=chr(97+b)

print(ans[::-1])
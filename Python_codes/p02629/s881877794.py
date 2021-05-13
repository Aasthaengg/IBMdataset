ini = lambda : int(input())
inm = lambda : map(int,input().split())
inl = lambda : list(map(int,input().split()))
gcd = lambda x,y : gcd(y,x%y) if x%y else y
n = ini()
b = ''
while n > 0:
        n -= 1
        b += chr(ord('a') + n%26)
        n = n//26
print(b[::-1])

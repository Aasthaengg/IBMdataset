n = int(input())

# 文字列参照用
c = "abcdefghijklmnopqrstuvwxyz"

ans = ""

while True:
    x = n % 26
    
    if x == 0:
        x = 26
    ans += c[x-1]
    
    n -= x
    
    if n == 0:
        break
        
    n //= 26
    
print(ans[::-1])
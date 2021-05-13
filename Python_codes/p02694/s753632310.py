x = int(input())

c = 100
ans = 0

while c < x:
    c = c + (c//100)
    ans += 1
    
print(ans)
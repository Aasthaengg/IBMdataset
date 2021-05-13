n = int(input())

ans = []
a = n
while a != 0:
    b = a % (-2)
    a //= (-2)
    if b == -1:
        a += 1
        b = 1
    ans.append(b)
if not ans: ans = [0]
ans.reverse()    
print(*ans, sep='')        

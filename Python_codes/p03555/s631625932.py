c1 = str(input())
c2 = str(input())
ans = 'NO'

if c1[0] == c2[2]:
    if c1[1] == c2[1]:
        if c1[2] == c2[0]:
            ans = 'YES'
            
print(ans)
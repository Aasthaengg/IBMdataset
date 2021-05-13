s = int(input())
ls = []
ls.append(s)
if s % 2 == 0:
    x = s//2
else:
    x = 3*s + 1
for i in range(10**6+1):
    if x in ls:
        ans = i+2
        break
    else:
        ls.append(x) 
        if x % 2 == 0:
            x = x//2
        else:
            x = 3*x + 1       
print(ans)
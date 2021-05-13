a,b,c,x = int(input()),int(input()),int(input()),int(input())
ans = 0
for i in range(min(a+1,41)):
    for j in range(min(b+1,201)):
        k = x-500*i-100*j
        if k >= 0 and k%50 == 0 and k//50 <= c:
            ans += 1
print(ans)
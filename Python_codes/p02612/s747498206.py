n = int(input())

m = 0
for i in range(12):
    if n > 1000*i:
        m = i
        
ans = 1000*(m+1) - n
print(ans)